import sys
input = sys.stdin.readline
def boj16928():
    n_ladder, n_snake = map(int, input().split())
    ladder_snake = list(list(map(int, input().split())) for _ in range(n_ladder + n_snake))
    ladder_snake.sort(key=lambda x: (x[1], x[1] - x[0]),reverse=True)
    pass
    print(*ladder_snake)
if __name__ == "__main__":
    boj16928()

