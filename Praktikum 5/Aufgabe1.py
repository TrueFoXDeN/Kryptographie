import math
import random
from Crypto.Util import number
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def generatePrime(length, iterations):
    elapsedtime = 0
    maxduration = 0
    for i in range(iterations):
        startiteration = time.time()

        number.getPrime(length)

        enditeration = time.time()
        currentduration = enditeration - startiteration
        elapsedtime += enditeration - startiteration

        if currentduration > maxduration:
            maxduration = currentduration

    averageduration = elapsedtime / iterations
    return averageduration, maxduration, elapsedtime


def rsa(length):
    p = number.getPrime(length)
    q = number.getPrime(length)
    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randrange(1, phi)
        if math.gcd(e, phi) == 1:
            break

    d = pow(e, -1, phi)
    # d = modInv(e, phi)
    return p, q, n, phi, e, d


def modInv(a, b):
    if b == 0:
        return a

    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while b > 0:
        q = a // b
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1

        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    return a


def testrsa(n, e, d, message):
    public_key = RSA.construct((n, e))
    private_key = RSA.construct((n, d))
    key_pair = RSA.construct((n, e, d))

    print(f'Public Key:  {public_key}')
    print(f'Private Key: {private_key}')
    print(f'Key Pair:    {key_pair}')

    encryptor = PKCS1_OAEP.new(public_key)
    message_encrypted = encryptor.encrypt(message)

    print(f'Encrypted Message: {message_encrypted}')

    decryptor = PKCS1_OAEP.new(key_pair)
    message_decrypted = decryptor.decrypt(message_encrypted)

    print(f'Decrypted Message: {message_decrypted}')

if __name__ == '__main__':
    # primeresult = generatePrime(1500, 10)
    # print(f'Average time: {primeresult[0]:.4f} seconds')
    # print(f'Max time:     {primeresult[1]:.4f} seconds')
    # print(f'Overall time: {primeresult[2]:.4f} seconds')

    p, q, n, phi, e, d = rsa(3000)
    print(f'p:   {p}')
    print(f'q:   {q}')
    print(f'n:   {n}')
    print(f'phi: {phi}')
    print(f'e:   {e}')
    print(f'd:   {d}')

    print('-------------')
    testrsa(n, e, d, b'30')
