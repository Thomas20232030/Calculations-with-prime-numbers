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


def atkins(limit):
    results = [2, 3, 5]
    sieve = [False] * (limit + 1)
    factor = int(math.sqrt(limit)) + 1
    for i in range(1, factor):
        for j in range(1, factor):
            n = 4 * i ** 2 + j ** 2
            if (n <= limit) and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * i ** 2 + j ** 2
            if (n <= limit) and (n % 12 == 7):
                sieve[n] = not sieve[n]
            if i > j:
                n = 3 * i ** 2 - j ** 2
                if (n <= limit) and (n % 12 == 11):
                    sieve[n] = not sieve[n]
    for index in range(5, factor):
        if sieve[index]:
            for jndex in range(index ** 2, limit, index ** 2):
                sieve[jndex] = False
    for index in range(7, limit):
        if sieve[index]:
            results.append(index)
    return results


grenze = 1000000000
sz = time.time()
print("Atkins")
atkins(grenze)
ez = time.time()
print(ez - sz)
sz = time.time()
print("Eratosthenes")
eratosthenes(grenze)
ez = time.time()
print(ez - sz)
