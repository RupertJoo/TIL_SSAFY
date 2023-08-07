def swea1989():
    for tc in range(1, int(input()) + 1):
        str1 = input()
        result = 1
        n = len(str1)
        for i in range(n // 2):
            # print(str1[i], str1[n - i - 1])
            if str1[i] != str1[n - i - 1]:

                result = 0
                break
        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea1989()