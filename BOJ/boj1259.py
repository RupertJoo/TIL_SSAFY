def boj1259():
    while True:
        x = input()
        if x == '0':
            break
        elif x == x[::-1]:
            print('yes')
        else:
            print('no')

    pass

if __name__ == "__main__":
    boj1259()