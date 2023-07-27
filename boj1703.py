import sys
input = sys.stdin.readline
def boj1703():
    while True:
        tree = list(map(int, input().split()))
        if tree[0] == 0:
            break
        else:
            value = 1
            for i in range(1, 2 * tree[0], 2):
                value *= tree[i]
                value -= tree[i + 1]
            sys.stdout.write(str(value) + '\n')

if __name__ == "__main__":
    boj1703()