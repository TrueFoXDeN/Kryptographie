import math


def encrypt(x, k, n):
    # Schlüssel wiederholen
    k = (k * math.ceil(len(x) / len(k)))[0:len(x)]
    x = convert(x)
    res = [0] * len(k)
    for i in range(len(k)):
        res[i] = (x[i] + k[i]) % n
    res = reconvert(res)
    return ''.join(res)


def decrypt(x, k, n):
    k = (k * math.ceil(len(x) / len(k)))[0:len(x)]
    x = convert(x)
    res = [0] * len(k)
    for i in range(len(k)):
        res[i] = (x[i] - k[i]) % n
    res = reconvert(res)
    return ''.join(res)


def convert(x):
    return [ord(a) - 65 for a in x]


def reconvert(x):
    return [chr(a + 65) for a in x]


x = 'WHYCRYPTOGRAPHYISHARDERTHANITLOOKS'
y = 'NVKGIMBXFUDEGVKMJVMVUSDXYOZMKZASBG'
k = convert(['R', 'O', 'M', 'E'])

print(encrypt(x, k, 26))
print(decrypt(y, k, 26))
