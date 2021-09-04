from main import sampleclient

# arg_reza = ['Gurux.DLMS.Client.Example.python/main.py', '-S', '/dev/ttyUSB0:19200:8Even1', '-g', '1.0.1.8.0.255:2',
#             '-c', '1', '-s', '17493', '-a', 'HighGMac', '-t', 'Verbose', '-T', '4D4D4D0000000001', '-v',
#             '0.0.43.1.0.255', '-C', 'AuthenticationEncryption', '-o',
#             'device.xml', '-G', 'sepanta']

# arg_reza = ['Gurux.DLMS.Client.Example.python/main.py', '-h', '193.105.234.168', '-p', '7370', '-g', '1.0.1.8.0.255:2',
#             '-c', '1', '-s', '17493', '-a', 'HighGMac', '-t', 'Verbose', '-T', '4D4D4D0000000001', '-v',
#             '0.0.43.1.0.255', '-C', 'AuthenticationEncryption', '-o',
#             'device.xml', '-G', 'sepanta']

arg_reza = ['Gurux.DLMS.Client.Example.python/main.py', '-h', 'localhost', '-p', '7370', '-g', '1.0.1.8.0.255:2',
            '-c', '1', '-s', '19369', '-a', 'HighGMac', '-t', 'Verbose', '-T', '4D4D4D0000000001', '-v',
            '0.0.43.1.0.255', '-C', 'AuthenticationEncryption', '-o',
            'device.xml', '-G', 'sepanta']

# arg_reza = ['Gurux.DLMS.Client.Example.python/main.py', '-S', '/dev/ttyUSB0:9600:8None1' , '-g', '1.0.1.8.0.255:2',
#             '-c', '1', '-s', '17493', '-a', 'HighGMac', '-t', 'Verbose', '-T', '4D4D4D0000000001', '-v',
#             '0.0.43.1.0.255', '-C', 'AuthenticationEncryption', '-o', 'tfc.xml']

# arg_reza = ['Gurux.DLMS.Client.Example.python/main.py', '-S', '/dev/ttyUSB0:9600:8None1' , '-g', '1.0.15.8.0.255:2;1.0.15.8.0.255:3',
#             '-c', '1', '-s', '19369', '-a', 'HighGMac', '-t', 'Verbose', '-T', '4D4D4D0000000001', '-v',
#             '0.0.43.1.0.255', '-C', 'AuthenticationEncryption', '-o', 'afzar.xml']


sampleclient.main(arg_reza)
