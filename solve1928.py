def solve1928():
    t = int(input())
    for i in range(1, t + 1):
        y = list(input())
        for j in y:
            print('0'+str(bin(ord(j)))[2:])
        print(f"#{i} {y}")
        pass
    pass

if __name__ == "__main__":
    solve1928()