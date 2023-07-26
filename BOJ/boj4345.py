# def boj4345():
#    while True:
#        try:
#             n = int(input())
#             str_1 = '1'
#             cnt = 1
#             while int(str_1) % n != 0:
#                 str_1 += '1'
#                 cnt += 1
#             print(cnt)
#             continue
#        except:
#            break

###

def boj4345():
    while True:
        try:
            n = int(input())
            x = 1
            cnt = 1
            while True:
                if x % n == 0:
                    print(cnt)
                    break
                else:
                    x = 10 * x + 1
                    cnt += 1
            
        except:
            break

if __name__ == "__main__":
    boj4345()

