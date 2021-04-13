import numpy as np

def encrypt(x, permutation):
    permutation = handlenotzero(permutation)
    chunksize = len(permutation)
    segments = [x[i:i + chunksize] for i in range(0, len(x), chunksize)]
    # print(segments, permutation, chunksize)
    arr = []
    for s in segments:
        arr.append(encryptsegment(s, permutation, chunksize))
    # Flatten und Leerzeichen entfernen, falls vorhanden
    res = ''.join(arr).replace(" ", "")
    return res


def encryptsegment(segment, permutation, chunksize):
    # Mit Leerzeichen auffüllen, falls Eingabe < Chunksize
    segment = segment + (" " * (chunksize - len(segment)))

    arr = [0] * chunksize

    for i in range(chunksize):
        arr[i] = segment[permutation[i]]

    res = ''.join(arr)

    return res


def handlenotzero(permutation):
    permutation = np.array(permutation)
    if 0 not in permutation:
        permutation -= 1
    return permutation.tolist()

def getinvolution(x, ps):
    for p in ps:
        d = encrypt(encrypt(x, p), p)
        if x == d:
            print(p)

# x = 'WHYCRYPTOGRAPHYISHARDERTHANITLOOKS'
# x = '8367649164'
# x = 'WUEHLMAEUSESINDINEUROPAASIENUNDNORDAMERIKAVERBREITETBEVORZUGTERLEBENSRAUMSINDLEICHTEBISMITTELSCHWEREBOEDENINDENENSIEOHNESCHWIERIGKEITENIHRGANGSYSTEMANLEGENKOENNENWOBEILOESSBOEDENBESONDERSBEVORZUGTWERDEN'
# p = [7, 8, 9, 2, 1, 0, 5, 4, 3, 6]
# p = [1, 3, 2]

# print(x)
# print(encrypt(x, p))
# print('------------')
# print(encrypt('WYHCYRPOTGARPYHIHSADRETRHNAILTOKOS', p))
# ps = set(permutations(p))

# getinvolution(x, ps)