import math
import time


def eratosthenes(end):
    end = end + 1
    primzahlliste = [True] * end
    primzahlliste[0] = False
    primzahlliste[1] = False

    for i in range(2, int(math.sqrt(end)) + 1):
        j = i * i
        while j < end:
            primzahlliste[j] = False
            j = j + i
    return [x for x in range(end) if primzahlliste[x] == True]


def primes(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]


for grenze in range(1000000, 10000000, 1000000):

    asz = time.time()
    primes(grenze)
    aez = time.time()
    ea = (aez - asz)

    esz = time.time()
    eratosthenes(grenze)
    eez = time.time()
    ee = eez - esz

    print(grenze, " / E1:", ea, "/ E2:", ee, "Prozent = ", (ea / ee) * 100, "%")

