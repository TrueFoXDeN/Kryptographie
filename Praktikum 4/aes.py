from Crypto.Cipher import AES
import binascii
from base64 import b64encode
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from itertools import product



def verifyAES():
    key = bytes.fromhex('2b7e151628aed2a6abf7158809cf4f3c')
    message = bytes.fromhex('3243f6a8885a308d313198a2e0370734')
    iv = bytes.fromhex('00000000000000000000000000000000')

    cipher = AES.new(key, AES.MODE_CBC, iv)

    ct_bytes = cipher.encrypt(message)

    ct = b64encode(ct_bytes).decode('utf-8')
    print(ct_bytes.hex())


def bruteforceAES():
    keypart = '5555555555555555555555555555'
    message = ''
    with open("data/chiffrat_AES.bin", "rb") as f:
        while byte := f.read(1):
            message = message + byte.hex()
    message = bytes.fromhex(message)
    iv = bytes.fromhex('808182838485868788898a8b8c8d8e8f')

    for s in values:
        try:
            s = ''.join(list(s))
            print(s)
            key = bytes.fromhex(s + keypart)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            # ct = cipher.decrypt(message)
            ct = unpad(cipher.decrypt(message), AES.block_size)
            # res = ct.decode("ASCII")
            hexct = binascii.b2a_hex(ct)
            if hexct.startswith(b'25 50 44 46 2D'):
                return hexct

        except:
            # print(s)
            continue


if __name__ == '__main__':
    hexvalues = []
    for i in range(32, 127):
        hexvalues.append(bytes([i]).hex())

    values = product(hexvalues, repeat=2)
    # print(values)
    print(bruteforceAES())