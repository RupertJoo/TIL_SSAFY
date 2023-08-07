import sys
sys.stdin = open("./refs/input_swea_1221.txt")

def countsort(arr, limit):
    len_arr = len(arr)
    arr_sorted = [None] * len_arr
    arr_count = [0] * (limit + 1)

    for i in range(len_arr):
        arr_count[arr[i]] += 1
    for i in range(1, limit + 1):
        arr_count[i] += arr_count[i - 1]
    for i in range(len_arr - 1, -1, -1):
        arr_count[arr[i]] -= 1
        arr_sorted[arr_count[arr[i]]] = arr[i]
    return arr_sorted


def swea1221():
    for tc in range(1, int(sys.stdin.readline()) + 1):
    # for tc in range(1, int(input()) + 1):
        _, n = input().split()
        n = int(n)
        arr_str = list(input().split())
        dict_num = {
                    "ZRO": 0,
                    "ONE": 1,
                    "TWO": 2,
                    "THR": 3,
                    "FOR": 4,
                    "FIV": 5,
                    "SIX": 6,
                    "SVN": 7,
                    "EGT": 8,
                    "NIN": 9
                    }
        dict_num_rev = {v: k for k, v in dict_num.items()}
        arr_convert = list(map(lambda x: dict_num[x], arr_str))
        arr_convert_sorted = countsort(arr_convert, 9)
        result = list(map(lambda x: dict_num_rev[x], arr_convert_sorted))
        print(f"{tc}")
        print(*result)


if __name__ =="__main__":
    swea1221()



def swea1221_2():
    # for tc in range(1, int(sys.stdin.readline()) + 1):
    for tc in range(1, int(input()) + 1):
        _, n = input().split()
        n = int(n)
        arr_str = list(input().split())
        dict_num = {
                    "ZRO": 0,
                    "ONE": 1,
                    "TWO": 2,
                    "THR": 3,
                    "FOR": 4,
                    "FIV": 5,
                    "SIX": 6,
                    "SVN": 7,
                    "EGT": 8,
                    "NIN": 9
                    }
        dict_num_rev = {v: k for k, v in dict_num.items()}

        arr_count = [0] * 10
        for i in arr_str:
            arr_count[dict_num[i]] += 1
        result = []
        for i in range(10):
            result += arr_count[i] * [dict_num_rev[i]]
        print(f"{tc}")
        print(*result)


if __name__ =="__main__":
    swea1221_2()