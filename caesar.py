def encrypt(x, k, alphabet):
    return ''.join(reconvert([(n + k) % alphabet for n in convert(x)]))


def decrypt(x, k, alphabet):
    return ''.join(reconvert([(n - k) % alphabet for n in convert(x)]))


def convert(x):
    return [ord(a) - 65 for a in x]


def reconvert(x):
    return [chr(a + 65) for a in x]


def crack(x):
    for i in range(26):
        print(decrypt(x, i, 26))


crack("ENWPZXEJQY")
print("----------")
print(decrypt("ENWPZXEJQY", 5, 26))
