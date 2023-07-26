def boj17427():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        ans += i * (n // i)
    return ans

if __name__ == "__main__":
    x = boj17427()
    print(x)
