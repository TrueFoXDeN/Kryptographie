import math
import numpy as np
import vigenere


def print_dict(dct):
    for key, value in dct.items():
        print("{}: {}".format(key, value))


def convert(x):
    return ord(x) - 65


def reconvert(x):
    return chr(x + 65)


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


#
# def speziellekoinzidenz(x, keylength):
#     p = np.array(
#         [0.174, 0.0978, 0.0755, 0.0727, 0.07, 0.0651, 0.0615, 0.0508, 0.0476, 0.0435, 0.0344, 0.0306, 0.0301, 0.0253,
#          0.0251, 0.0189, 0.0189, 0.0166, 0.0121, 0.0113, 0.0079, 0.0067, 0.0031, 0.0027, 0.0004, 0.0003, 0.0002])
#
#     c = []
#     for i in range(keylength):
#         c.append(x[i::keylength])
#     koninz = 0
#     for g in range(1):
#         for chunk in c:
#             chunk = list(chunk)
#
#             dic = {i: chunk.count(i) for i in chunk}
#             val = 0
#             for key, value in dic.items():
#                 val += p[convert(key)] * value
#
#             k = val / len(chunk)
#             koninz += k
#
#         koninz /= keylength
#     return koninz

def recunstructkey(x, keylength):
    germandist = ["E", "N", "I", "S", "R", "A", "T", "D", "H", "U", "L", "C", "G", "M", "O", "B", "W", "F", "K", "Z",
                  "P", "V", "J", "Y", "X", "Q"]

    # Vigenere-Quadrat Tabelle erstellen
    alphabet = [chr(x + 65) for x in range(26)]
    vigenerequadrat = np.array(alphabet)

    for i in range(1, 26):
        shiftedalphabet = np.roll(alphabet, shift=-i, axis=0)
        vigenerequadrat = np.row_stack((vigenerequadrat, shiftedalphabet))
    # print(vigenerequadrat)

    c = []
    for i in range(keylength):
        c.append(x[i::keylength])

    key = []
    for chunk in c:
        chunk = list(chunk)
        # print(chunk)
        dic = {i: chunk.count(i) for i in chunk}

        sorted_tuples = sorted(dic.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = {k: v for k, v in sorted_tuples}
        # print(sorted_dict)
        mostusedchar = next(iter(sorted_dict.keys()))
        shift = 0
        shiftend = 0

        for k in sorted_dict.keys():
            if shift == shiftend:
                mostusedchar = k
                break
            shift += 1

        for i in range(26):
            if mostusedchar == vigenerequadrat[i][alphabet.index(germandist[shift])]:
                key.append(alphabet[i])
                break

    # print("['I', 'X', 'B', 'Q', 'H', 'Y', 'G', 'J', 'L', 'V']")
    print(key)
    key = 'IXBQHYGJLV'
    print(vigenere.decrypt(x, vigenere.convert(key), 26))


f = open("data/chiffrat2.txt", "r")
x = f.read()
# x = 'NVKGIMBXFUDEGVKMJVMVUSDXYOZMKZASBG'
# print(f'Koinzidenz: {koinzidenz(x, 5):.4f}')
# koinzidenz(x, 5)
# reconstructkeylength(x, 4, 11)
# print(speziellekoinzidenz(x, 4))
recunstructkey(x, 10)
