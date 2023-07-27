import sys
input = sys.stdin.readline
def boj20529():
    for _ in range(int(input())):
        n = int(input())
        distance = 0
        list_mbti = list(map(set, input().split()))
        len_mbti = len(list_mbti)
        if n > 32:
            print(0)
        else:
            common = 0
            for i in range(len_mbti):
                for j in range(i + 1, len_mbti):
                    for k in range(j + 1, len_mbti):
                        common_mbti = len(list_mbti[i] & list_mbti[j]) + len(list_mbti[i] & list_mbti[k]) + len(list_mbti[j] & list_mbti[k])
                        if common  < common_mbti:
                            common = common_mbti
            sys.stdout.write(str(12 - common) + '\n')

    pass

if __name__ == "__main__":
    boj20529()