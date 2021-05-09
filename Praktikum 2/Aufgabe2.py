def Decrypt(ciphertext1, ciphertext2, ciphertext3):
    text1 = []
    text2 = []
    text3 = []

    for c1, c2, c3 in zip(ciphertext1, ciphertext2, ciphertext3):
        text1.append(ord(c1))
        text2.append(ord(c2))
        text3.append(ord(c3))

    t1_xor_t2 = []
    t1_xor_t3 = []
    t2_xor_t3 = []

    for t1, t2, t3 in zip(text1, text2, text3):
        t1_xor_t2.append(t1 ^ t2)
        t1_xor_t3.append(t1 ^ t3)
        t2_xor_t3.append(t2 ^ t3)

    assert(len(text1) == len(text2) == len(text3))
    textlength = len(text1)

    #################
    # Crib Dragging
    #################
    guessword = [ord(c) for c in "Corona"]
    for shift in range(textlength - len(guessword) + 1):
        #Alle drei XOR Arrays durchprobieren
        print(f'Shift {shift:2.0f}:', end=' ')
        for array in [t1_xor_t2, t1_xor_t3, t2_xor_t3]:
            encryptedSublist = array[shift:shift + len(guessword):]
            decryptedList = []
            for a, b in zip(guessword, encryptedSublist):
                res = a ^ b
                decryptedList.append(res)

            decryptedText = ''.join([chr(c) for c in decryptedList])
            print(f'{decryptedText}', end=' ')
        print()


if __name__ == '__main__':
    f = open("data/chiffrat2.txt").read()
    encryptedText = f.split()
    Decrypt(encryptedText[0], encryptedText[1], encryptedText[2])
