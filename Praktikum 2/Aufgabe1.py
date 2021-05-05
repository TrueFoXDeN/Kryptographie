import numpy as np
import time

def bitwise_xor_bytes(a, b):
    result_int = int.from_bytes(a, byteorder="big") ^ int.from_bytes(b, byteorder="big")
    return result_int.to_bytes(max(len(a), len(b)), byteorder="big")


def Decrypt(ciphertext, key):
    encryptedBytes = []
    with open("data/chiffrat.bin", "rb") as f:
        while byte := f.read(1):
            encryptedBytes.append(int.from_bytes(byte, "big"))

    schluesselstrom = []
    with open("data/random.dat", "rb") as f:
        while byte := f.read(1):
            schluesselstrom.append(int.from_bytes(byte, "big"))

    # print(encryptedBytes)
    start = time.time()
    for shift in range(10000, 20000):
        decrypted = []
        for b, s in zip(encryptedBytes, schluesselstrom[shift::]):
            decrypted.append(b ^ s)

        decryptedText = [chr(x) for x in decrypted]
        decryptedText = ''.join(decryptedText)

        if 'and' in decrypted:
            print(f'found at {shift}')
            return

        # print(f'Checking: {shift}')
    end = time.time()
    print(f'Time elapsed for 10000 iterations: {end-start:.0f}s')
    # print(schluesselstrom)
    # a = bytes([0x00, 0x01, 0x02, 0x03])
    # b = bytes([0x03, 0x02, 0x01, 0xff])
    # print(type(a))
    # decrypted = bitwise_xor_bytes(a,b)
    # decrypted = bitwise_xor_bytes(encryptedBytes, schluesselstrom)

    # print(decrypted)


if __name__ == '__main__':
    Decrypt("a", "b")
