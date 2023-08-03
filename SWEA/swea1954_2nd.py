def swea1954_2nd():
    for tc in range(1, int(input()) + 1):
        n = int(input())
        arr = list(list([0] * n) for _ in range(n))
        move = [[0, 1],
                [1, 0],
                [0, -1],
                [-1, 0]]
        idx = 0
        r, c = 0, 0
        for i in range(1, n ** 2 + 1):
            # 다음 위치를 먼저 정의하고 이 값으로 비교해야 한다!
            arr[r][c] = i
            nr = r + move[idx][0]
            nc = c + move[idx][1]
            if 0 <= nr < n and 0<= nc < n and arr[nr][nc] == 0: # 쇼트서킷의 순서가 달라질 경우 배열 인덱스 초과로 오류가 발생한다!
                r, c = nr, nc
            else:
                idx = (idx + 1) % 4 # 0,1,2,3 -> 1,2,3,0
                r = r + move[idx][0]
                c = c + move[idx][1]

        print(f"#{tc}")
        for i in arr:
            print(*i)

if __name__ == "__main__":
    swea1954_2nd()