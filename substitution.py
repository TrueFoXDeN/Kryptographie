import numpy as np


def encrypt(x, key):
    alphabet = [reconvert(a) for a in range(26)]
    res = ''
    for s in x:
        res += key[alphabet.index(s)]
    return res


def decrypt(x, key):
    alphabet = [reconvert(a) for a in range(26)]
    res = ''
    for s in x:
        res += alphabet[key.index(s)]
    return res


def convert(x):
    return ord(x) - 65


def reconvert(x):
    return chr(x + 65)


print(encrypt('BAHNHOFBONN',
              ['X', 'N', 'Y', 'A', 'H', 'P', 'O', 'G', 'Z', 'Q', 'W', 'B', 'T', 'S', 'F', 'L', 'R', 'C', 'V', 'M', 'U',
               'E', 'K', 'J', 'D', 'I']))

print(decrypt('NXGSGFPNFSS',
              ['X', 'N', 'Y', 'A', 'H', 'P', 'O', 'G', 'Z', 'Q', 'W', 'B', 'T', 'S', 'F', 'L', 'R', 'C', 'V', 'M', 'U',
               'E', 'K', 'J', 'D', 'I']))
