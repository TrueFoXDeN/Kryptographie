def LFSR(initialwerte, durchlaeufe):
    assert len(initialwerte) == 21
    zustand = initialwerte.copy()
    naechsterzustand = zustand.copy()
    res = []
    periode = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
    toleranz = 1
    for i in range(durchlaeufe):
        for j in range(20, 0, -1):
            naechsterzustand[j - 1] = zustand[j]
        naechsterzustand[20] = zustand[0] ^ zustand[19]

        zustand = naechsterzustand.copy()
        if zustand == periode:
            if toleranz == 0:
                return i, zustand
            toleranz -= 1

        #res.append(zustand[0])
    #print(res)


if __name__ == '__main__':
    print(LFSR([1] * 21, 3000000))
