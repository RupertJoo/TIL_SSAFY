
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


def boj1837():
    pq, k = map(int, input().split())
    # 
    if pq % 2 == 0:
        p, q = 2, pq // 2
    elif pq % 3 == 0:
        p, q = 3, pq // 3
    else:
        isBreak = False
        while isBreak == False:
            # print('sex')
            # for i in range(3, int(pq ** 0.5) + 1, 2):
            # primelist = primeList(int(pq ** 0.5) + 1)
            # print(primelist)
            for i in  primeList(int(pq ** 0.5) + 1):    
                # print(i)
                if pq % i == 0:
                    p = i
                    q = pq // i
                    isBreak = True
                    break
            break 
    if p < k:
        return print(f"BAD {p}")   
    else:
        return print("GOOD")
# 
if __name__ == "__main__":
    boj1837()