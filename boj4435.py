import sys
def boj4435():
    input = sys.stdin.readline
    for i in range(1, int(input()) + 1):
        heroes = list(map(int, input().split()))
        villains = list(map(int, input().split()))

        scores_h = [1, 2, 3, 3, 4, 10]
        scores_v = [1, 2, 2, 2, 3, 5, 10]

        total_h = sum(list(map(lambda x, y: x * y, heroes, scores_h)))
        total_v = sum(list(map(lambda x, y: x * y, villains, scores_v)))

        if total_h > total_v:
            sys.stdout.write("Battle " + str(i) + ": Good triumphs over Evil" + '\n')
        elif total_h < total_v:
            sys.stdout.write("Battle " + str(i) + ": Evil eradicates all trace of Good" + '\n')
        else:
            sys.stdout.write("Battle " + str(i) + ": No victor on this battle field" + '\n')

if __name__ == "__main__":
    boj4435()