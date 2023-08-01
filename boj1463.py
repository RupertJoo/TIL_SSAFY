def boj1463():
    n = int(input())
    ans = 0
    while n > 1:
        
        if (is3 := sum(list(map(int, list(str(n))))) % 3) == 0:
            n //= 3
            ans += 1
        elif n % 3 == 1:
            pass
        elif n % 3 == 2:
            pass
    print(ans)
            

if __name__ == "__main__":
    boj1463()