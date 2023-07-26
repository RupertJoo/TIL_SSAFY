import sys
def boj11650():
    list_xy = []
    
    for _ in range(int(input())):
        list_xy.append(list(map(int, sys.stdin.readline().split())))
    # list_xy = sorted(list_xy, key=lambda xy: xy[0])
    # for i in range(len(list_xy) - 1):
    #     if list_xy[i][0] == list_xy[i + 1][0]:
    #         if list_xy[i][1] > list_xy[i + 1][1]:
    #             list_xy[i][1], list_xy[i + 1][1] = list_xy[i + 1][1], list_xy[i][1]
    list_xy = sorted(list_xy)
    for j in list_xy:
        sys.stdout.write(str(j[0])+ ' ' + str(j[1]) + '\n')            
if __name__ == "__main__":
    boj11650()