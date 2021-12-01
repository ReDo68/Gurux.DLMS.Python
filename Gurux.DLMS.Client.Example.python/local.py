from sepanta_dlms import RezaV4


obj = RezaV4()
obj.media = 'Serial'
obj.device = 'meter'   #gw
my_arg = {'company': 'tfc',
        'server_addr': 14865 ,
        'authentication': 'HighGMac' ,
        'policy':  'AuthenticationEncryption',
        # 'fc_obis':  ,
        # 'system_title':  ,
        'EKey': '00000000000000000000000000000000' ,
        'AKey': '00000000000000000000000000000000' ,
        # 'port_num':  ,
        # 'server_invoke':  ,
        # 'gw_frame_counter':  ,
        # 'frame_counter':  ,
        # 'get_with_list':  ,
        # 'meter_baud':  ,
        # 'password':  ,
        'obis':  '0.0.1.0.0.255:2',
        # 'com_test':
          }

# my_arg = {'company': 'tfc',
#         'server_addr': 14865 ,
#         'authentication': 'Low' ,
#         'policy':  'None',
#         # 'fc_obis':  ,
#         # 'system_title':  ,
#         # 'EKey': '00000000000000000000000000000000' ,
#         # 'AKey': '00000000000000000000000000000000' ,
#         # 'port_num':  ,
#         # 'server_invoke':  ,
#         # 'gw_frame_counter':  ,
#         # 'frame_counter':  ,
#         # 'get_with_list':  ,
#         # 'meter_baud':  ,
#         'password': '87654321' ,
#         # 'obis': '0.0.1.0.0.255:2' ,
#         # 'com_test':
#           }

obj.read_def(my_arg)



        # SMART LLS
        # arg = ['Gurux.DLMS.Client.Example.python/main.py', '-c', self.client_addr, '-s', self.server_addr,
        #        '-a', 'Low', '-P', '87654321', '-t', 'Verbose',
        #        '-T', '4D4D4D0000000001', '-v', '0.0.43.1.0.255', '-C', 'None',
        #        '-N', self.port_num, '-V', self.server_invoke, '-W', self.gw_frame_counter,
        #        '-F', self.frame_counter, '-L', self.get_with_list,
        #        '-A', '74577AD8E39FF641EEDACDFB94C34AC3',
        #        '-B', 'A6BF5D3CB17E52FD431215B8B7F1C6CC']

        # SMART HighGMac
        # arg = ['Gurux.DLMS.Client.Example.python/main.py', '-c', self.client_addr, '-s', self.server_addr,
        #        '-a', 'HighGMac', '-P', '87654321', '-t', 'Verbose',
        #        '-T', '4D4D4D0000000001', '-v', '0.0.43.1.0.255', '-C', 'AuthenticationEncryption',
        #        '-N', self.port_num, '-V', self.server_invoke, '-W', self.gw_frame_counter,
        #        '-F', self.frame_counter, '-L', self.get_with_list,
        #        '-A', '00000000000000000000000000000000',
        #        '-B', '00000000000000000000000000000000']

