import Aufgabe1


def chinesischer_restsatz(p, q, n, d, x):
    xp = x % p
    xq = x % q
    dp = d % (p - 1)
    dq = d % (q - 1)

    yp = pow(xp, dp, p)
    yq = pow(xq, dq, q)

    cp = pow(q, -1, p)
    cq = pow(p, -1, q)

    print(n)
    return (q * cp * yp + p * cq * yq) % n


if __name__ == '__main__':
    p, q, n, phi, e, d = Aufgabe1.rsa(3000)
    cr = chinesischer_restsatz(p, q, n, d, 30)
    print(cr)
    Aufgabe1.testrsa(n, e, d, b'30')
