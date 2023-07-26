
'''
import sys
def boj10814():
    list_xy = []
    
    for i in range(int(input())):
        list_xy.append([sys.stdin.readline().split(), i])
        list_xy[i][0][0] = int(list_xy[i][0][0])
    list_xy.sort(key=lambda x:(x[0][0], x[1]))
    # for j in range(len(list_xy)-1):
    #     if list_xy[j][0][0] == list_xy[j+1][0][0] and list_xy[j][1] > list_xy[j + 1][1]:
    #         list_xy[j], list_xy[j + 1] = list_xy[j + 1], list_xy[j]
        # elif list_xy[j][0][0] == list_xy[j+1][0][0]:
        #     pass    
    # print(*list_xy)
    for j in list_xy:
        sys.stdout.write(str(j[0][0])+ ' ' + str(j[0][1]) + '\n')            
if __name__ == "__main__":
    boj10814()
'''

import sys

def boj10814():
    input = sys.stdin.readline
    list_age_name = [input() for _ in range(int(input()))]
    list_age_name.sort(key=lambda x: int(x.split()[0]))
    print("".join(list_age_name))
if __name__ =="__main__":
    boj10814()