import sys
def boj1181():
    input = sys.stdin.readline
    list_words = list(set(input().strip() for _ in range(int(input()))))
    # sys.stdout.write(list_words)
    list_words.sort(key=lambda x: (len(x), x))
    # print(*(i for i in list_words), sep='\n')
    for i in list_words:
        sys.stdout.write(i + '\n')
if __name__ =="__main__":
    boj1181()