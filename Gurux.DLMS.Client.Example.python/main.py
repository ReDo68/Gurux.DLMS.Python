#
#  --------------------------------------------------------------------------
#   Gurux Ltd
#
#
#
#  Filename: $HeadURL$
#
#  Version: $Revision$,
#                   $Date$
#                   $Author$
#
#  Copyright (c) Gurux Ltd
#
# ---------------------------------------------------------------------------
#
#   DESCRIPTION
#
#  This file is a part of Gurux Device Framework.
#
#  Gurux Device Framework is Open Source software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 2 of the License.
#  Gurux Device Framework is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#  See the GNU General Public License for more details.
#
#  More information of Gurux products: http://www.gurux.org
#
#  This code is licensed under the GNU General Public License v2.
#  Full text may be retrieved at http://www.gnu.org/licenses/gpl-2.0.txt
# ---------------------------------------------------------------------------
import os
import sys
import traceback
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
    #pylint: disable=broad-except
except Exception:
    #It's OK if this fails.
    print("pkg_resources not found")

#pylint: disable=too-few-public-methods,broad-except
class sampleclient():
    @classmethod
    def main(cls, args):
        try:
            pass
            # print("gurux_dlms version: " + pkg_resources.get_distribution("gurux_dlms").version)
            # print("gurux_net version: " + pkg_resources.get_distribution("gurux_net").version)
            # print("gurux_serial version: " + pkg_resources.get_distribution("gurux_serial").version)
        except Exception:
            #It's OK if this fails.
            print("pkg_resources not found")


        readout_str = b'READOUT\r\n'
        # args: the command line arguments
        reader = None
        settings = GXSettings()
        try:
            # //////////////////////////////////////
            #  Handle command line parameters.
            # print(args)
            ret = settings.getParameters(args)
            if ret != 0:
                return
            # print(settings.outputFile.split(".")[0])
            # //////////////////////////////////////
            #  Initialize connection settings.
            if not isinstance(settings.media, (GXSerial, GXNet)):
                raise Exception("Unknown media type.")
            # //////////////////////////////////////
            reader = GXDLMSReader(settings.client, settings.media, settings.trace,
                                  settings.invocationCounter, settings.iec,
                                  settings.gwWrapper, settings.port_num, settings.server_invoke)
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
                    reader.getAssociationView()
                for k, v in settings.readObjects:
                    print("------------>", k, v)
                    obj = settings.client.objects.findByLN(ObjectType.NONE, k)
                    if obj is None:
                         raise Exception("Unknown logical name:" + k)
                    val = reader.read(obj, v)
                    print("value is: ", val)
                    reader.showValue(v, val)
                    try:
                        val = bytes(val)
                    except:
                        val = str(val).encode()

                    # print(val)
                    readout_str += b'%b(%b)\r\n' % (k.encode(), val)
                    # if isinstance(val, (bytes, bytearray)):
                    #     readout_str += b'%b(%b)\r\n' % (k.encode(), str(val).encode())
                    # elif isinstance(val, list):
                    #     readout_str += b'%b(%b)\r\n' % (k.encode(), bytearray.fromhex(str(val)))
                    # else:
                    #     print("else")

                readout_str += b'IDMSG(%b)\r\n' % (settings.outputFile.split(".")[0]).encode()
                print(readout_str)
                if settings.outputFile:
                    settings.client.objects.save(settings.outputFile)
            else:
                reader.readAll(settings.outputFile)
        except (ValueError, GXDLMSException, GXDLMSExceptionResponse, GXDLMSConfirmedServiceError) as ex:
            print(ex)
        except (KeyboardInterrupt, SystemExit, Exception) as ex:
            traceback.print_exc()
            settings.media.close()
            reader = None
        finally:
            if reader:
                try:
                    if settings.outputFile.split(".")[0] == 'eaa':
                        reader.disconnect()
                    else:
                        reader.close()

                    settings.media.send(gwWrap(readout_str, 0, 0))
                    settings.media.close()
                except Exception:
                    traceback.print_exc()
            print("Ended. Press any key to continue.")

class ReadV4:
    def __init__(self, meter_type, physical, port_num=1 , server_invoke=0):
        self.meter_type = meter_type  # 'tfc' 'eaa'
        self.OBIS = '1.0.0.0.0.255:2;1.0.1.8.0.255:2;1.0.1.8.1.255:2;1.0.1.8.2.255:2;1.0.1.8.3.255:2'
        # self.OBIS = '0.0.20.0.0.255:2;0.0.20.0.0.255:3;0.0.20.0.0.255:4;0.0.20.0.0.255:5;' \
        #             '0.2.22.0.0.255:7;0.2.22.0.0.255:8'   Timming
        self.device = 'gw'  # 'gw' 'meter'
        self.media = 'TCP'  # 'TCP' 'Serial'
        self.server_addr = str(16384+physical)    #'19369'  # 0x4000+physical(1000+sn_last_4digits)

        self.client_addr = '1'
        self.ip = 'localhost'  #'193.105.234.168'  'localhost'
        self.port = '7370'
        self.usb = "/dev/ttyUSB0"
        self.port_num = str(port_num)
        self.server_invoke = str(server_invoke)

    def read(self):
        arg = ['Gurux.DLMS.Client.Example.python/main.py', '-c', self.client_addr, '-s', self.server_addr, '-a', 'HighGMac', '-t', 'Verbose',
               '-T', '4D4D4D0000000001', '-v', '0.0.43.1.0.255', '-C', 'AuthenticationEncryption',
               '-N', self.port_num, '-V', self.server_invoke]

        if self.device == 'gw':
            self.usb = self.usb+":19200:8Even1"
            arg = arg + ['-G', 'sepanta']
        elif self.device == 'meter':
            self.usb = self.usb + ":9600:8None1"
        else:
            print("Please choose between 'gw' and 'meter' mode in device")

        if self.media == 'TCP':
            arg = arg + ['-h', self.ip, '-p', self.port]
        elif self.media == 'Serial':
            arg = arg + ['-S', self.usb]
        else:
            print("Please choose between 'TCP' and 'Serial' mode in media")

        if self.OBIS:
            arg = arg + ['-g', self.OBIS]

        if self.meter_type == 'tfc':
            arg = arg + ['-o', 'tfc.xml']
        elif self.meter_type == 'eaa':
            arg = arg + ['-o', 'eaa.xml']
        else:
            print("Please choose a correct meter_type EX: afzar")

        return arg

def callreadv4(company, physical, port, serverinvoke):
    sampleclient.main(ReadV4(company, physical, port, serverinvoke).read())
# print(read_v4('tfc').read())
# sampleclient.main(ReadV4('tfc', 2985, 1, 0).read())  #1110


# if __name__ == '__main__':
#     arg_reza = ['Gurux.DLMS.Client.Example.python/main.py', '-S', '/dev/ttyUSB0:19200:8Even1', '-g', '1.0.1.8.0.255:2',
#                 '-c', '1', '-s', '17493', '-a', 'HighGMac', '-t', 'Verbose', '-T', '4D4D4D0000000001', '-v',
#                 '0.0.43.1.0.255', '-C', 'AuthenticationEncryption', '-o',
#                 '/home/reza/Documents/Project/dlms/device.xml', '-G', 'sepanta']
#
#     # sampleclient.main(arg_reza)
#     sampleclient.main(sys.argv)
