import sys
# sys.stdin = open("in.txt", "r")

for tc in range(1, int(input()) + 1):
    N = int(input())

    list_dr = [-1, 1, 0, 0]
    list_dc = [0, 0, -1, 1]

    for dc, dr in zip(list_dr, list_dc):
        print(dc, dr)
        # nr = r + dr
        # nc = c + dc

    # if 0 <= nr < N and 0 <= nc < N:
    #     pass

# if x < 0: x *= -1
