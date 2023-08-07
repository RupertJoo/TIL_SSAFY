def swea16346():
    for tc in range(1, int(input()) + 1):
        str1 = input()
        str2 = input()

        m = len(str1)
        n = len(str2)
        result = 0
        for i in range(n - m + 1):
            ptn = str2[i:i + m]
            # print(ptn)
            if ptn == str1:
                result = 1
                break
        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea16346()