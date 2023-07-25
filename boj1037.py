def boj1037():
    _ = int(input())
    x = set(map(int, input().split(' ')))
    print(max(x) * min(x))

if __name__ == "__main__":
    boj1037()