import numpy as np
from itertools import permutations
import re


def checkifkeyvalid(x):
    keywords = ["DIE", "DER", "UND", "IM", "ZU", "DEN", "DAS"]
    return all(s in x for s in keywords)


def crack(x, dist):
    alphabet = [chr(x) for x in range(65, 91)]
    currentdist = {}
    for a in alphabet:
        currentdist[a] = x.count(a)
    currentdist = {k: v for k, v in sorted(currentdist.items(), key=lambda item: item[1], reverse=True)}
    vals = list(currentdist.keys())

    p = np.array(list(currentdist.values())) / 3114
    ref = np.array(
        [0.174, 0.0978, 0.0755, 0.0727, 0.07, 0.0651, 0.0615, 0.0508, 0.0476, 0.0435, 0.0344, 0.0306, 0.0301, 0.0253,
         0.0251, 0.0189, 0.0189, 0.0166, 0.0121, 0.0113, 0.0079, 0.0067, 0.0031, 0.0027, 0.0004, 0.0003, 0.0002])
    soldist = ["V", "Q", "O", "U", "N", "K", "M", "B", "C", "F", "W", "G", "E", "T", "D", "X", "H", "I", "A", "J", "P",
               "R", "Z", "L", "Y", "S"]

    # print(vals)
    print(p)
    print(ref)
    print(vals)
    print(soldist)
    print(dist)
    res = ""
    for s in x:
        if re.match("[A-Z]+", s):
            res += s
        else:
            res += dist[soldist.index(s)]
    # zipped = zip(currentdist, dist)
    # mappedvalues = dict(zipped)

    # print(mappedvalues)
    print(checkifkeyvalid(res))
    return res


f = open("data/chiffrat.txt", "r")
text = f.read().replace("Ä", "AE").replace("Ü"),
germandist = ["E", "N", "I", "S", "R", "A", "T", "D", "H", "U", "L", "C", "G", "M", "O", "B", "W", "F", "K", "Z", "P",
              "V", "J", "Y", "X", "Q"]
modifieddist = ["E", "N", "S", "A", "I", "R", "U", "D", "H", "U", "L", "C", "G", "M", "O", "B", "W", "F", "K", "Z", "P",
                "V", "J", "Y", "X", "Q"]

print(crack(text, germandist))
