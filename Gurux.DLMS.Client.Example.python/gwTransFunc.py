import math, codecs
from Crypto.Cipher import AES

def calCrc(inStr, inLen):
    dnpCrcTable = [
        0x0000, 0x3D65, 0x7ACA, 0x47AF, 0xF594, 0xC8F1, 0x8F5E, 0xB23B, 0xD64D, 0xEB28, 0xAC87, 0x91E2, 0x23D9,
        0x1EBC, 0x5913, 0x6476, 0x91FF, 0xAC9A, 0xEB35, 0xD650, 0x646B, 0x590E, 0x1EA1, 0x23C4, 0x47B2, 0x7AD7,
        0x3D78, 0x001D, 0xB226, 0x8F43, 0xC8EC, 0xF589, 0x1E9B, 0x23FE, 0x6451, 0x5934, 0xEB0F, 0xD66A, 0x91C5,
        0xACA0, 0xC8D6, 0xF5B3, 0xB21C, 0x8F79, 0x3D42, 0x0027, 0x4788, 0x7AED, 0x8F64, 0xB201, 0xF5AE, 0xC8CB,
        0x7AF0, 0x4795, 0x003A, 0x3D5F, 0x5929, 0x644C, 0x23E3, 0x1E86, 0xACBD, 0x91D8, 0xD677, 0xEB12, 0x3D36,
        0x0053, 0x47FC, 0x7A99, 0xC8A2, 0xF5C7, 0xB268, 0x8F0D, 0xEB7B, 0xD61E, 0x91B1, 0xACD4, 0x1EEF, 0x238A,
        0x6425, 0x5940, 0xACC9, 0x91AC, 0xD603, 0xEB66, 0x595D, 0x6438, 0x2397, 0x1EF2, 0x7A84, 0x47E1, 0x004E,
        0x3D2B, 0x8F10, 0xB275, 0xF5DA, 0xC8BF, 0x23AD, 0x1EC8, 0x5967, 0x6402, 0xD639, 0xEB5C, 0xACF3, 0x9196,
        0xF5E0, 0xC885, 0x8F2A, 0xB24F, 0x0074, 0x3D11, 0x7ABE, 0x47DB, 0xB252, 0x8F37, 0xC898, 0xF5FD, 0x47C6,
        0x7AA3, 0x3D0C, 0x0069, 0x641F, 0x597A, 0x1ED5, 0x23B0, 0x918B, 0xACEE, 0xEB41, 0xD624, 0x7A6C, 0x4709,
        0x00A6, 0x3DC3, 0x8FF8, 0xB29D, 0xF532, 0xC857, 0xAC21, 0x9144, 0xD6EB, 0xEB8E, 0x59B5, 0x64D0, 0x237F,
        0x1E1A, 0xEB93, 0xD6F6, 0x9159, 0xAC3C, 0x1E07, 0x2362, 0x64CD, 0x59A8, 0x3DDE, 0x00BB, 0x4714, 0x7A71,
        0xC84A, 0xF52F, 0xB280, 0x8FE5, 0x64F7, 0x5992, 0x1E3D, 0x2358, 0x9163, 0xAC06, 0xEBA9, 0xD6CC, 0xB2BA,
        0x8FDF, 0xC870, 0xF515, 0x472E, 0x7A4B, 0x3DE4, 0x0081, 0xF508, 0xC86D, 0x8FC2, 0xB2A7, 0x009C, 0x3DF9,
        0x7A56, 0x4733, 0x2345, 0x1E20, 0x598F, 0x64EA, 0xD6D1, 0xEBB4, 0xAC1B, 0x917E, 0x475A, 0x7A3F, 0x3D90,
        0x00F5, 0xB2CE, 0x8FAB, 0xC804, 0xF561, 0x9117, 0xAC72, 0xEBDD, 0xD6B8, 0x6483, 0x59E6, 0x1E49, 0x232C,
        0xD6A5, 0xEBC0, 0xAC6F, 0x910A, 0x2331, 0x1E54, 0x59FB, 0x649E, 0x00E8, 0x3D8D, 0x7A22, 0x4747, 0xF57C,
        0xC819, 0x8FB6, 0xB2D3, 0x59C1, 0x64A4, 0x230B, 0x1E6E, 0xAC55, 0x9130, 0xD69F, 0xEBFA, 0x8F8C, 0xB2E9,
        0xF546, 0xC823, 0x7A18, 0x477D, 0x00D2, 0x3DB7, 0xC83E, 0xF55B, 0xB2F4, 0x8F91, 0x3DAA, 0x00CF, 0x4760,
        0x7A05, 0x1E73, 0x2316, 0x64B9, 0x59DC, 0xEBE7, 0xD682, 0x912D, 0xAC48]

    crc = 0
    for i in range(inLen):
        crc = ((crc << 8) ^ dnpCrcTable[((crc >> 8) ^ inStr[i]) & 0x00FF]) & 0xFFFF
    crc ^= 0xFFFF
    return bytes([int(crc / 256) & 0xFF, crc & 0xFF])

def gwWrap(data, port_num, server_invoke, gw_frame_counter):
    print(gw_frame_counter)
    dataL = len(data) + 12
    totLen = math.ceil((dataL + 4) / 16) * 16
    totLen += 3
    port = int(port_num)
    # 0: 300, 3: 2400, 4: 4800, 5: 9600, 6: 19200
    initBd = 5
    # In ms
    waitTime = 500
    bitNum = 8
    # 0: None, 1: Odd, 2: Even
    parity = 0
    recLen = 1000
    sendStr = b'\x7E'
    sendStr += bytes([int(totLen / 256), totLen % 256])
    sendStr += b'\x00\x05'
    sendStr += bytes([int(dataL / 256), dataL % 256])
    sendStr += gw_frame_counter  # bytes.fromhex(gw_frame_counter)  # b'\x04\xdd'  # Frame Counter
    sendStr += bytes([port])
    sendStr += bytes([int(int(server_invoke) / 256), int(server_invoke) % 256])
    sendStr += bytes([initBd])
    sendStr += bytes([int(waitTime / 256), waitTime % 256])
    sendStr += bytes([bitNum, parity])
    sendStr += bytes([int(recLen / 256), recLen % 256])
    sendStr += data
    sendStr += bytes(totLen - dataL - 7)
    sendStr += calCrc(sendStr[3:], totLen - 3)
    sendStr += b'\x7E'
    return sendStr

def gwUnwrap(str):
    if len(str) < 22:
        return None
    length = str[5]*256 + str[6] - 12
    return str[19:19+length]
    # return codecs.getencoder('hex')(str[19:19+length])[0]


# def gw_enc():
#     encryptor = AES.new(b'6841654163243084', AES.MODE_ECB)
#     rcvData = rcvData[:3] + encryptor.decrypt(rcvData[3:int((len(rcvData) - 6) / 16) * 16 + 3]) + rcvData[int((len(rcvData) - 6) / 16) * 16 + 3:]
#     encryptor = AES.new(b'6841654163243084', AES.MODE_ECB)
#     rcvData = encryptor.decrypt(rcvData)
def gw_encryption(rcvData):
    encryptor = AES.new(b'6841654163243084', AES.MODE_ECB)
    rcvData = rcvData[:3] + encryptor.encrypt(rcvData[3:])
    rcvData += calCrc(rcvData[3:], len(rcvData) - 3)
    rcvData += b'\x7E'

    return rcvData

def gw_decryption(rcvData):
    encryptor = AES.new(b'6841654163243084', AES.MODE_ECB)
    rcvData = rcvData[:3] + encryptor.decrypt(rcvData[3:-3]) + rcvData[-3:]

    return rcvData