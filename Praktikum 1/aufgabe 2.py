import math
import numpy as np


def print_dict(dct):
    for key, value in dct.items():
        print("{}: {}".format(key, value))


def koinzidenz(x, l):
    # print(f'Koinzidenz berechnen für {x} mit Schlüssellänge {l}')

    c = []
    for i in range(l):
        c.append(x[i::l])

    koninz = 0
    # print(f'Chunk splitting: {c}')
    # print('-------------------')
    for chunk in c:
        chunk = list(chunk)
        # print(chunk)
        dic = {i: chunk.count(i) for i in chunk}
        duplikate = 0
        for v in dic.values():
            if v > 1:
                duplikate += v * (v - 1)
        k = duplikate / (len(chunk) * (len(chunk) - 1))
        koninz += k
        # print(f'Berechne: {duplikate} / ({len(chunk)} * {len(chunk) - 1})')
        # print(f'Teil-Koinzidenz: {k:.3f}')
        # print('-------------------')
    koninz /= l
    return koninz


def reconstructkeylength(x, min, max):
    print('Rekonstruiere Key-Length mittels Koinzidenz:')
    print()
    d = {}
    for i in range(min, max + 1):
        k = koinzidenz(x, i)
        d[i] = k
        print(f'Koinzidenz für Schlüssellänge {i}: {k}')
        # print('---------------------')
    print()
    # print(f'Berechnete Schlüssel:')
    # print_dict(d)
    v = list(d.values())
    k = list(d.keys())

    curr = 0
    for i in v:
        if i > curr:
            curr = i
    mostprob = k[v.index(curr)]

    print(f'Wahrscheinlichste Schlüssellänge: {mostprob}')


f = open("data/chiffrat2.txt", "r")
x = f.read()
# x = 'NVKGIMBXFUDEGVKMJVMVUSDXYOZMKZASBG'
# print(f'Koinzidenz: {koinzidenz(x, 5):.4f}')
reconstructkeylength(x, 4, 11)

