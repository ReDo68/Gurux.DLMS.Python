from sepanta_dlms import RezaV4


obj = RezaV4()
obj.media = 'Serial'
obj.device = 'meter'   # gw
# obj.client_addr = 1   # 16 1 DABGER!!!!!!!!!!!!!!!!!!!!

# TFC 19200 public
my_arg = {'company': 'tfc',
        # 'server_addr':  ,  #????????
        'authentication': 'None',  #'HighGMac' ,
        'policy': 'None' ,  #'AuthenticationEncryption',
        # 'fc_obis':  ,
        # 'system_title':  ,
        # 'EKey': '00000000000000000000000000000000' ,
        # 'AKey': '00000000000000000000000000000000' ,
        # 'port_num':  ,
        # 'server_invoke':  ,
        # 'gw_frame_counter':  ,
        # 'frame_counter':  ,
        # 'get_with_list':  ,
        # 'meter_baud': 6 ,
          'usb': "/dev/ttyUSB0" + ":19200:8None1",
        # 'password':  ,
        'obis':  '0.0.42.0.0.255:2',
        # 'com_test':
          }

# TFC 19200 Manage
my_arg = {'company': 'tfc',
        'server_addr': 1109 , #?????????
        'authentication': 'HighGMac',  #'HighGMac' ,
        'policy': 'AuthenticationEncryption' ,  #'AuthenticationEncryption',
        # 'fc_obis':  ,
        # 'system_title':  ,
        # 'EKey': '00000000000000000000000000000000' ,
        # 'AKey': '00000000000000000000000000000000' ,
        # 'port_num':  ,
        # 'server_invoke':  ,
        # 'gw_frame_counter':  ,
        # 'frame_counter':  ,
        # 'get_with_list':  ,
        # 'meter_baud': 6 ,
          'usb': "/dev/ttyUSB0" + ":19200:8None1",
        # 'password':  ,
        'obis':  '0.0.42.0.0.255:2',
        # 'com_test':
          }

# TFC 19200 Manage without physical :-D
my_arg = {'company': 'tfc',
        'server_addr': 1-16384 , #?????????
        'authentication': 'HighGMac',  #'HighGMac' ,
        'policy': 'AuthenticationEncryption' ,  #'AuthenticationEncryption',
        # 'fc_obis':  ,
        # 'system_title':  ,
        # 'EKey': '00000000000000000000000000000000' ,
        # 'AKey': '00000000000000000000000000000000' ,
        # 'port_num':  ,
        # 'server_invoke':  ,
        # 'gw_frame_counter':  ,
        # 'frame_counter':  ,
        # 'get_with_list':  ,
        # 'meter_baud': 6 ,
          'usb': "/dev/ttyUSB0" + ":19200:8None1",
        # 'password':  ,
        'obis':  '0.0.42.0.0.255:2',
        # 'com_test':
          }



# SMART HighGMac
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

obj.read_def(my_arg)


# SMART LLS

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
