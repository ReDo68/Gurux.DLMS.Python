from main import sampleclient

class ReadV4:
    def __init__(self, meter_type, physical):
        self.meter_type = meter_type  # 'tfc' 'afzar'
        self.OBIS = '1.0.1.8.0.255:1;1.0.1.8.0.255:2;1.0.1.8.0.255:3'
        self.device = 'gw'  # 'gw' 'meter'
        self.media = 'TCP'  # 'TCP' 'Serial'
        self.server_addr = str(16384+physical)    #'19369'  # 0x4000+physical(1000+sn_last_4digits)

        self.client_addr = '1'
        self.ip = 'localhost'  #'193.105.234.168'  'localhost'
        self.port = '7370'
        self.usb = "/dev/ttyUSB0"
        self.client_addr = '1'

    def read(self):
        arg = ['Gurux.DLMS.Client.Example.python/main.py', '-a', 'HighGMac', '-t', 'Verbose',
               '-T', '4D4D4D0000000001', '-v', '0.0.43.1.0.255', '-C', 'AuthenticationEncryption']

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
        elif self.meter_type == 'afzar':
            arg = arg + ['-o', 'afzar.xml']
        else:
            print("Please choose a correct meter_type EX: afzar")

        return arg

# print(read_v4('tfc').read())
sampleclient.main(ReadV4('tfc', 1110).read())

# arg_reza = ['Gurux.DLMS.Client.Example.python/main.py', '-S', '/dev/ttyUSB0:19200:8Even1', '-g', '1.0.1.8.0.255:2',
#             '-c', '1', '-s', '19369', '-a', 'HighGMac', '-t', 'Verbose', '-T', '4D4D4D0000000001', '-v',
#             '0.0.43.1.0.255', '-C', 'AuthenticationEncryption', '-o',
#             'device.xml', '-G', 'sepanta']

# local - gw - tfc
# arg_reza = ['Gurux.DLMS.Client.Example.python/main.py','-S', '/dev/ttyUSB0:19200:8Even1',
#             '-g', '1.0.1.8.0.255:1;1.0.1.8.0.255:2;1.0.1.8.0.255:3',
#             '-c', '1', '-s', '19369', '-a', 'HighGMac', '-t', 'Verbose', '-T', '4D4D4D0000000001', '-v',
#             '0.0.43.1.0.255', '-C', 'AuthenticationEncryption', '-o',
#             'tfc.xml', '-G', 'sepanta']

# local - gw - Afzar
# arg_reza = ['Gurux.DLMS.Client.Example.python/main.py', '-S', '/dev/ttyUSB0:19200:8Even1',
#             '-g', '1.0.1.8.0.255:1;1.0.1.8.0.255:2;1.0.1.8.0.255:3',
#             '-c', '1', '-s', '19369', '-a', 'HighGMac', '-t', 'Verbose',
#             '-T', '4D4D4D0000000001', '-v', '0.0.43.1.0.255',
#             '-C', 'AuthenticationEncryption', '-o', 'afzar.xml',
#             '-G', 'sepanta']

# local - direct - Afzar
# arg_reza = ['Gurux.DLMS.Client.Example.python/main.py', '-S', '/dev/ttyUSB0:9600:8None1',
#             '-g', '1.0.1.8.0.255:1;1.0.1.8.0.255:2;1.0.1.8.0.255:3',
#             '-c', '1', '-s', '19369', '-a', 'HighGMac', '-t', 'Verbose',
#             '-T', '4D4D4D0000000001', '-v', '0.0.43.1.0.255',
#             '-C', 'AuthenticationEncryption', '-o', 'afzar.xml']

# arg_reza = ['Gurux.DLMS.Client.Example.python/main.py', '-h', '193.105.234.168', '-p', '7370', '-g', '1.0.1.8.0.255:2',
#             '-c', '1', '-s', '17493', '-a', 'HighGMac', '-t', 'Verbose', '-T', '4D4D4D0000000001', '-v',
#             '0.0.43.1.0.255', '-C', 'AuthenticationEncryption', '-o',
#             'device.xml', '-G', 'sepanta']

# arg_reza = ['Gurux.DLMS.Client.Example.python/main.py', '-h', 'localhost', '-p', '7370', '-g', '1.0.1.8.0.255:1;1.0.1.8.0.255:2;1.0.1.8.0.255:3',
#             '-c', '1', '-s', '19369', '-a', 'HighGMac', '-t', 'Verbose', '-T', '4D4D4D0000000001', '-v',
#             '0.0.43.1.0.255', '-C', 'AuthenticationEncryption', '-o',
#             'device.xml', '-G', 'sepanta']

# arg_reza = ['Gurux.DLMS.Client.Example.python/main.py', '-S', '/dev/ttyUSB0:9600:8None1' , '-g', '1.0.1.8.0.255:2',
#             '-c', '1', '-s', '17493', '-a', 'HighGMac', '-t', 'Verbose', '-T', '4D4D4D0000000001', '-v',
#             '0.0.43.1.0.255', '-C', 'AuthenticationEncryption', '-o', 'tfc.xml']

# arg_reza = ['Gurux.DLMS.Client.Example.python/main.py', '-S', '/dev/ttyUSB0:9600:8None1' , '-g', '1.0.15.8.0.255:2;1.0.15.8.0.255:3',
#             '-c', '1', '-s', '19369', '-a', 'HighGMac', '-t', 'Verbose', '-T', '4D4D4D0000000001', '-v',
#             '0.0.43.1.0.255', '-C', 'AuthenticationEncryption', '-o', 'afzar.xml']