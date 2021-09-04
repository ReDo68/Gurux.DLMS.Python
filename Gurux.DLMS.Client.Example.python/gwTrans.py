import serial
import serial.tools.list_ports, re
import time, math, codecs
from crc import *

# temp = serial.tools.list_ports.comports(include_links=False)
# for dev in temp:
#     print(dev.device)
#

# print(temp[0].device)
# ser = serial.Serial(temp[0].device, baudrate=19200, bytesize=8, timeout=2, parity=serial.PARITY_EVEN, rtscts=0)
# ser = serial.Serial("/dev/ttyUSB0", baudrate=19200, bytesize=8, timeout=2, parity=serial.PARITY_EVEN, rtscts=0)
ser = serial.Serial("/dev/ttyUSB0", baudrate=19200, bytesize=8, timeout=2, parity=serial.PARITY_NONE, rtscts=0)
data = b'\x7e\xa0\x0a\x00\x02\x10\xab\x03\x93\x14\x68\x7e'
        #    type+len  addr-up addr-lo addr-cli snrm
# data2 = b'\x2f\x3f12341234\x21\x0d\x0a'
dataL = len(data) + 12
totLen = math.ceil((dataL + 4) / 16) * 16
totLen += 3
port = 1
# port = int(input('port: '))
initBd = 5
# initBd = int(input('bd: '))
waitTime = 700
# waitTime = int(input('waitTime: '))
bitNum = 8
# bitNum = int(input('bitNum: '))
parity = 0
# parity = int(input('parity: '))
recLen = 100
# recLen = int(input('recLen: '))
sendStr = b'\x7E'
sendStr += bytes([int(totLen / 256), totLen % 256])
sendStr += b'\x00\x05'
sendStr += bytes([int(dataL / 256), dataL % 256])
sendStr += b'\x32\xF7'
sendStr += bytes([port])
sendStr += bytes(2)
sendStr += bytes([initBd])
sendStr += bytes([int(waitTime / 256), waitTime % 256])
sendStr += bytes([bitNum, parity])
sendStr += bytes([int(recLen / 256), recLen % 256])
sendStr += data
# sendStr += data
sendStr += bytes(totLen - dataL - 7)
sendStr += calCrc(sendStr[3:], totLen - 3)
sendStr += b'\x7E'
# print(sendStr)
# ser.write(sendStr)
print(data)
ser.write(data)
# time.sleep(1)
# sendStr=b'PL'
# ser.write(sendStr)
# time.sleep(1)
rcv = ser.read(200)
print(rcv)
if len(rcv) > 22:
    print(codecs.getencoder('hex')(rcv[19:-3])[0])
