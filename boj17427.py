'''
두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.

자연수 N이 주어졌을 때, g(N)을 구해보자.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력
첫째 줄에 g(N)를 출력한다.


'''
def makeListPrime(x):
    ans = set()
    ans.add(0)
    for i in range (1, x + 1):
        ans.add(isPrime(i))
    ans.remove(0)
    return ans
    pass

def isPrime(x):
    if x < 2:
        return 0
    elif x == 2:
        return x
    elif x % 2 == 0:
        return 0
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




def boj17427():
    n = int(input())
    listPrime = makeListPrime(n)
    gn = 0
    for i in range(1,n + 1):
        # 보다 일반적으로, 보다 간단하게
        gn += funF(i, listPrime)
    print(gn)

def funF(x, listPrime):
    ans = 0
    if x == 1:
        ans += x
        return ans
    else:
        # for i in range(1, x // 2+ 1):
        #     if x % i == 0:
        #         ans += i
        dict_prime = {}
        ans = 1
        for i in listPrime:
            while x >= i and x % i == 0:
                dict_prime.setdefault(i,0)
                dict_prime[i] += 1
                x = x // i
        # print(f'{x}// {dict_prime}')
        for j in dict_prime:
            
            ans *= aaa(j,dict_prime[j])
        return ans



    pass
if __name__ == "__main__":
    boj17427()

