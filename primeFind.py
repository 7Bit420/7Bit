maxPrime = 10_000_000


def isPrime(p):
    l = True
    for n in range(2, p - 1):
        if (p % n == 0):
            l = False
            break
    return l


for i in range(2, maxPrime):
    if isPrime(i):
        print(i)
