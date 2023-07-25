def makeListPrime(x):
    ans = []
    for i in range (1, x + 1):
        if isPrime(i) != 0:
            ans.append(i)
    return ans
    pass

def isPrime(x):
    if x < 2 or x % 2 == 0:
        return 0
    elif x == 2:
        return x
    elif x == 3:
        return x
    else:
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return 0
        return x
    
def aaa(a, b):
    ans = 0
    for i in range(b + 1):
        ans += a ** i
    return ans

if __name__ == "__main__":
    # x = int(input())
    # print(makeListPrime(x))
    a, b = map(int, input().split(' '))
    print(aaa(a,b))



