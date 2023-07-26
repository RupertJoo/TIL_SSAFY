def primeList(n):
    # n = int(input())
    primes = [0] * 2 + list(range(2,n + 1))
    i = 1
    for j in range(2,n + 1):
        if primes[j] != 0:
            for k in range(2 * j, n + 1, j):
                primes[k] = 0
    primes = list(filter(lambda x: x != 0,primes ))
    return primes

pp = 