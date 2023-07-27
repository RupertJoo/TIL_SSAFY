'''
# def boj2609():
#     MAX = 10000
#     MAX = int(input())
#     isprime = [False] * 2 + list(range(2, MAX + 1))
    
#     for i in range(2, MAX + 1):
#         if isprime[i] != 0:
#             for j in range(i * 2,MAX + 1,i):
#                 isprime[j] = 0
#             # print(*(isprime))
#     print(*(i for i in isprime if i != 0))

            
    
#     pass

# if __name__ == "__main__":
#     boj2609()
'''
#유클리드 호제법으로 최대공약수(GCD)를 구한다.
# 두 자연수의 곱은 최대공약수와 최소공배수의 곱과 같으므로
# 최소공배수(LCM) = 두 자연수의 곱 // GCD

def boj2609():
    a, b = map(int,input().split())
    list_ab = [a,b]
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    gcd = a + b
    lcm = (list_ab[0] * list_ab[1]) // gcd
    print(gcd, lcm,sep='\n')
    pass

if __name__ == "__main__":
    boj2609()