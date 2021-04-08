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


def koinzidenz(x):
    alphabet = [chr(x) for x in range(65, 91)]
    dist = {}

    for a in alphabet:
        dist[a] = x.count(a)

    f = []
    for key, val in dist.items():
        f.append(val)

    n = len(alphabet)
    res = 0

    for i in range(n):
        res += math.comb(f[i], 2)

    res /= math.comb(len(x), 2)
    return res


def reconstructkeylength(x, p):
    alphabet = [chr(x) for x in range(65, 91)]
    dist = {}

    for a in alphabet:
        dist[a] = x.count(a)

    f = []
    for key, val in dist.items():
        f.append(val)

    n = len(alphabet)
    res = 0
    values = []
    for g in range(27):
        for i in range(n):
            res += (f[i]/len(x)) * f[min(i+g, len(f)-1)]
        res /= len(x)
        values.append(res)
        print(res)
    return values.index(max(values))


x = 'WHYCRYPTOGRAPHYISHARDERTHANITLOOKS'
y = 'NVKGIMBXFUDEGVKMJVMVUSDXYOZMKZASBG'
z = 'WUEHLMAEUSESINDINEUROPAASIENUNDNORDAMERIKAVERBREITETBEVORZUGTERLEBENSRAUMSINDLEICHTEBISMITTELSCHWEREBOEDENINDENENSIEOHNESCHWIERIGKEITENIHRGANGSYSTEMANLEGENKOENNENWOBEILOESSBOEDENBESONDERSBEVORZUGTWERDEN'
k = convert(['R', 'O', 'M', 'E'])

# print(encrypt(x, k, 26))
# print(decrypt(y, k, 26))

p = koinzidenz(y)
print(p)
print('---------')
g = reconstructkeylength(y, p)
print('---------')
print(g)
#4 Buchstaben: 0.03929853085039343
#5 Buchstaben: 0.03835307097656867