import sys
sys.stdin = open("./refs/input_swea_16266.txt")

def swea16266():
    # for tc in range(1, int(input()) + 1):
    for tc in range(1, int(sys.stdin.readline()) + 1):
        n, k = map(int, input().split())
        dozen = list(range(1, 12 + 1))
        result = 0
        for i in range(1 << 12): # 경우의 수는 2^12
            arr3 = []
            for j in range(12): # 배열 dozen에 있는 0 ~ 11번째 요소들에 대해
                if i & (1 << j): # 어떤 경우의 수에 배열 요소들이 있다면
                    arr3.append(dozen[j]) # 배열 dozen에 가산한다.
            # print(arr3)
            if len(arr3) == n:
                sum_elm3 = 0
                for elm3 in arr3:
                    sum_elm3 += elm3
                if sum_elm3 == k: # 요소의 갯수가 3인 배열의 합이 k일 때, 반환값에 1을 더한다.
                    result += 1
        print(f"#{tc} {result}")

if __name__ == "__main__":
    swea16266()