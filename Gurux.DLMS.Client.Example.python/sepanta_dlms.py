"""
Note:
    Please consider reading RezaBook for more information
    Gurux is a 4 byte addressing that means --> Server address = physical + 16384 or 4+(pysical-HEX) so I'm adding the 16384 to the physical inside code so don't need to do anything else
        Ex: my TFC smart meter physical is: 14865  --> just put 14865 inside db physical addr
        Ex:

"""
import os
import math
import sys
import traceback
import pandas as pd
from gurux_serial import GXSerial
from gurux_net import GXNet
from gurux_dlms.enums import ObjectType
from gurux_dlms.objects.GXDLMSObjectCollection import GXDLMSObjectCollection
from GXSettings import GXSettings
from GXDLMSReader import GXDLMSReader
from gurux_dlms.GXDLMSClient import GXDLMSClient
from gurux_common.GXCommon import GXCommon
from gurux_dlms.enums.DataType import DataType
import locale
from gurux_dlms.GXDateTime import GXDateTime
from gurux_dlms.internal._GXCommon import _GXCommon
from gurux_dlms import GXDLMSException, GXDLMSExceptionResponse, GXDLMSConfirmedServiceError
from gwTransFunc import calCrc, gwWrap, gwUnwrap


try:
    import pkg_resources
except Exception as e:
    print("pkg_resources not found", e)


class RezaV4:
    def __init__(self):

        self.device             = 'gw'                    # 'gw' 'meter'
        self.media              = 'TCP'                   # 'TCP' 'Serial'
        self.client_addr        = 1
        self.ip                 = 'localhost'             # ***mandatory-1*** '193.105.234.168'  'localhost'
        self.port               = '7370'                  # ***mandatory-1***
        self.usb                = "/dev/ttyUSB0"          # ***mandatory-1***
        self.valid_producer     = ['tfc', 'eaa']

        # Default OBIS
        # self.OBIS = '1.0.0.0.0.255:2;1.0.1.8.0.255:2;1.0.1.8.1.255:2;1.0.1.8.2.255:2;1.0.1.8.3.255:2'
        self.OBIS = '0.0.1.0.0.255:2;0.0.42.0.0.255:2;1.0.1.8.0.255:2;1.0.1.8.1.255:2;1.0.1.8.2.255:2;' \
                    '1.0.1.8.3.255:2;1.0.1.8.4.255:2;1.0.32.7.0.255:2;1.0.31.7.0.255:2'
        #             '1.0.32.7.0.255:2;1.0.31.7.0.255:2;1.0.2.8.0.255:2'
        # self.OBIS = '0.0.20.0.0.255:2;0.0.20.0.0.255:3;0.0.20.0.0.255:4;0.0.20.0.0.255:5;' \
        #             '0.2.22.0.0.255:7;0.2.22.0.0.255:8'   Timming

    def read_def(self, server_args):
        # print('read_def --> ', server_args)
        server_args['com_test'] = 1
        # Create system arg
        arg = {'loging': 'Verbose'}

        if self.device == 'gw':
            self.usb = self.usb+":19200:8Even1"
            arg['gateway'] = 'sepanta'
        elif self.device == 'meter':
            self.usb = self.usb + ":9600:8None1"
        else:
            print("Please choose between 'gw' and 'meter' mode in device")

        if self.media == 'TCP':
            arg['host'] = self.ip
            arg['port'] = self.port
        elif self.media == 'Serial':
            arg['usb'] = self.usb
        else:
            print("Please choose between 'TCP' and 'Serial' mode in media")

        # updating server_args
        if 'obis' not in server_args:
            server_args['obis'] = self.OBIS

        if 'company' in server_args:
            if server_args['company'] in self.valid_producer:
                arg['output'] = server_args['company'] + '.xml'
            else:
                print("Please choose a '''correct''' company EX: afzar")
        else:
            print("Please choose a company EX: afzar")

        if 'server_addr' in server_args:
            server_args['client_addr'] = self.client_addr
            # '19369'  # 0x4000+physical(1000+sn_last_4digits)
            if int(server_args['server_addr']) != 1:
                server_args['server_addr'] = 16384+int(server_args['server_addr'])

        if 'com_test' in server_args:
            if server_args['com_test'] == 1:
                try:
                    # print(os.getcwd())
                    pd.options.mode.chained_assignment = None
                    df = pd.read_csv('/root/ct.csv')
                    print(df.T)
                except:
                    print("------ CSV not found! -----")

                try:
                    if not self.isNaN(df['meter_baud'][0]):
                        server_args['meter_baud'] = int(df['meter_baud'][0])
                    if not self.isNaN(df['server_addr'][0]):
                        server_args['server_addr'] = 16384+int(df['server_addr'][0])
                    if not self.isNaN(df['client_addr'][0]):
                        server_args['client_addr'] = int(df['client_addr'][0])
                    if not self.isNaN(df['authentication'][0]):
                        server_args['authentication'] = df['authentication'][0]
                    if not self.isNaN(df['policy'][0]):
                        server_args['policy'] = df['policy'][0]
                    if not self.isNaN(df['EKey'][0]):
                        server_args['EKey'] = df['EKey'][0]
                    if not self.isNaN(df['AKey'][0]):
                        server_args['AKey'] = df['AKey'][0]
                    if not self.isNaN(df['obis'][0]):
                        server_args['obis'] = df['obis'][0]
                    if not self.isNaN(df['password'][0]):
                        server_args['password'] = str(df['password'][0])
                    if not self.isNaN(df['port_num'][0]):
                        server_args['port_num'] = int(df['port_num'][0])
                    if not self.isNaN(df['system_title'][0]):
                        server_args['system_title'] = df['system_title'][0]
                    if not self.isNaN(df['fc_obis'][0]):
                        server_args['fc_obis'] = df['fc_obis'][0]

                except Exception as e:
                    print("------ CSV not applied! -----> Exception: ", e)


        # consider server_args as:
        #     Name            default                           type    choices          check by
        # company*            -                                 str    ['eaa', 'tfc']    valid_producer
        # server_addr*        miss means: public client         int
        # authentication     'None'                             str    [None Low High HighMd5 HighSha1 HighGMac HighSha256]
        # policy             'None'                             str    [None Authentication Encryption AuthenticationEncryption]
        # fc_obis            '0.0.43.1.0.255'                   str
        # system_title       '4D4D4D0000000001'                 str
        # EKey               'D0D1D2D3D4D5D6D7D8D9DADBDCDDDEDF' str
        # AKey               '000102030405060708090A0B0C0D0E0F' str
        # port_num           1                                  int
        # server_invoke      0                                  int
        # gw_frame_counter   b'\x04\xdd'                        byte?
        # frame_counter      0                                  int
        # get_with_list      0                                  int     [0, 1]
        # meter_baud         5                                  int     [0,3,4,5,6]
        # password*          miss means: Not Low level Auth     str
        # obis               Reza OBIS List                     str     'obis:att;'
        # com_test           0                                  int     [0, 1]

        arg.update(server_args)
        self.main(arg)

    @classmethod
    def main(cls, args):
        # print('main --> ', args)
        try:
            pass
            # print("gurux_dlms version: " + pkg_resources.get_distribution("gurux_dlms").version)
            # print("gurux_net version: " + pkg_resources.get_distribution("gurux_net").version)
            # print("gurux_serial version: " + pkg_resources.get_distribution("gurux_serial").version)
        except Exception as e:
            print("pkg_resources not found", e)  # It's OK if this fails.

        readout_str = b'READOUT\r\n'
        reader = None
        settings = GXSettings()
        try:
            # Handle  parameters.
            ret = settings.get_parameters(args)
            if ret != 0:
                return
            # Initialize connection settings.
            if not isinstance(settings.media, (GXSerial, GXNet)):
                raise Exception("Unknown media type.")
            # settings.client.serverAddressSize = 1
            # settings.client.__setserverAddressSize = 1
            # define reader acording to settings
            reader = GXDLMSReader(settings.client, settings.media, settings.trace, settings.invocationCounter,
                                  settings.gwWrapper, settings.port_num, settings.server_invoke,
                                  settings.frame_counter, settings.get_with_list, settings.gw_frame_counter,
                                  settings.meter_baud)
            settings.media.open()
            if settings.readObjects:
                read = False
                reader.initializeConnection()
                if settings.outputFile and os.path.exists(settings.outputFile):
                    try:
                        c = GXDLMSObjectCollection.load(settings.outputFile)
                        settings.client.objects.extend(c)
                        if settings.client.objects:
                            read = True
                    except Exception:
                        read = False
                if not read:
                    print("getgetPAssociationView in the main")
                    reader.getAssociationView()

                if settings.get_with_list == 1 :
                    print('+++++++++++++++ GETTTING WITH LIIIST +++++++++++++++')
                    list_arr = []
                    for k, v in settings.readObjects:
                        obj = settings.client.objects.findByLN(ObjectType.NONE, k)
                        if obj is None:
                            raise Exception("Unknown logical name:" + k)
                        list_arr += (obj, v)

                    list_arr = [x for x in zip(*[iter(list_arr)] * 2)]
                    val_list = reader.readList(list_arr)

                    # sending readout
                    m = 0
                    for k, v in settings.readObjects:
                        val = val_list[m]
                        m += 1
                        val = reader.readout_value(val)
                        print(k, v, " = ", val)
                        readout_str += b'%b(%b)\r\n' % (k.encode(), val)

                else:
                    for k, v in settings.readObjects:
                        obj = settings.client.objects.findByLN(ObjectType.NONE, k)
                        if obj is None:
                             raise Exception("Unknown logical name:" + k)
                        val = reader.read(obj, v)
                        print("------------>", k, v)
                        reader.showValue(v, val)
                        val = reader.readout_value(val)

                        readout_str += b'%b(%b)\r\n' % (k.encode(), val)

                fc_val = str(settings.client.ciphering.invocationCounter + 2).encode()
                readout_str += b'fc(%b)\r\n' % fc_val
                readout_str += b'IDMSG(%b)\r\n' % (settings.outputFile.split(".")[0]).encode()
                print(readout_str)

                if settings.outputFile:
                    print("Skip saving on the output")
                    # settings.client.objects.save(settings.outputFile)
                    pass
            else:
                reader.readAll(settings.outputFile)
        except (ValueError, GXDLMSException, GXDLMSExceptionResponse, GXDLMSConfirmedServiceError) as ex:
            print(ex)
        except (KeyboardInterrupt, SystemExit, Exception) as ex:
            traceback.print_exc()
            if settings.media:
                settings.media.close()
            reader = None
        finally:
            if reader:
                try:
                    try:
                        if settings.outputFile.split(".")[0] == 'eaa':
                            reader.disconnect()
                        else:
                            reader.close()
                    except:
                        reader.close()

                    settings.media.send(gwWrap(readout_str, 0, 0, settings.gw_frame_counter, settings.meter_baud))
                    if settings.media:
                        settings.media.close()
                except Exception:
                    traceback.print_exc()

            print("Ended!")

    @staticmethod
    def isNaN(num):
        return num != num




def callreadv4(server_arg):
    obj = RezaV4()
    obj.read_def(server_arg)
    # SampleClient.main(ReadV4(company, physical, port, serverinvoke, framecounter, getwithlist, gwfc).read())