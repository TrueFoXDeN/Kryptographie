from Crypto.Cipher import AES
import binascii
from base64 import b64encode
from Crypto.Util.Padding import pad

key = bytes.fromhex('2b7e151628aed2a6abf7158809cf4f3c')
message = bytes.fromhex('3243f6a8885a308d313198a2e0370734')
iv = bytes.fromhex('00000000000000000000000000000000')

cipher = AES.new(key, AES.MODE_CBC, iv)

ct_bytes = cipher.encrypt(message)

print(ct_bytes.hex())
ct = b64encode(ct_bytes).decode('utf-8')
