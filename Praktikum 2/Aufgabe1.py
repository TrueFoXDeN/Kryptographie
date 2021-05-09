import numpy as np
import time

def Decrypt(ciphertext, key):
    encryptedBytes = []
    with open(ciphertext, "rb") as f:
        while byte := f.read(1):
            encryptedBytes.append(int.from_bytes(byte, "big"))

    schluesselstrom = []
    with open(key, "rb") as f:
        while byte := f.read(1):
            schluesselstrom.append(int.from_bytes(byte, "big"))

    # print(encryptedBytes)
    start = time.time()
    iterations = 2500000
    toleranzgrenze = 10
    aktuelltolieriert = toleranzgrenze

    for shift in range(iterations):
        decrypted = []
        valid = True
        listToSearch = zip(encryptedBytes, schluesselstrom[shift:shift + len(encryptedBytes):])
        for b, s in listToSearch:
            res = b ^ s
            if res < 32 or res > 128:
                if aktuelltolieriert == 0:
                    valid = False
                    break
                aktuelltolieriert -= 1

            decrypted.append(b ^ s)
        aktuelltolieriert = toleranzgrenze
        if valid:
            decryptedText = [chr(x) for x in decrypted]
            decryptedText = ''.join(decryptedText)
            end = time.time()
            print(f'Time elapsed for {shift} iterations: {end - start:.0f}s')

            return decryptedText
        else:
            decrypted.clear()

    end = time.time()
    print(f'Time elapsed for {iterations} iterations: {end - start:.0f}s')


if __name__ == '__main__':
    print(Decrypt("data/chiffrat.bin", "data/random.dat"))
