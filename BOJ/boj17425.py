# def boj17425():
#     for _ in range(int(input())):
#         n = int(input())
#         ans = 0
#         for i in range(1, n + 1):
#             ans += i * (n // i)
#         print(ans)
    


# if __name__ == "__main__":
#     x = boj17425()
'''
import sys
def boj17425():
    MAX = int(1e6)
    list_fx = [0] * (MAX + 1)
    list_gx = [0] * (MAX + 1)

    for i in range(1, MAX + 1):
        j = 1
        for k in range(i*j, MAX + 1, i*j):
            list_fx[k] += i
            j += 1
        list_gx[i] = list_gx[i -1] + list_fx[i]

    for _ in range(int(input())):
        n = int(sys.stdin.readline())
        sys.stdout.write(str(list_gx[n]) + "\n")
if __name__ == "__main__":
    boj17425()
'''

import sys

MAX = int(1e6)
list_fx = [0] * (MAX + 1)
list_gx = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    j = 1
    for k in range(i*j, MAX + 1, i*j):
        list_fx[k] += i
        j += 1
    list_gx[i] = list_gx[i -1] + list_fx[i]
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    sys.stdout.write(str(list_gx[n]) + "\n")