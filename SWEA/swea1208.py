def counting_sort(dumps, n, max_height): # 배열과 배열의 길이, 배열이 가질 수 있는 최대값을 인수로 받아 카운팅정렬된 배열을 반환한다.
    # n = 100
    # max_height = 100
    arr_count = [0] * (max_height + 1) #카운트 배열의 길이는 0 ~ max_height
    arr_sorted = [None] * n # 정렬된 배열의 길이는 원본 배열의 길이와 같다.
    # dump[i]를 인덱스로 갖는 배열 arr_count에 1씩 더해준다
    # 이는 인덱스 및 인덱스값이 각각 dumps의 요소 값과 그 갯수에 대응한다.
    for i in range(n):
        arr_count[dumps[i]] += 1 # 누적합을 요소로 갖도록 한다.      
    for i in range(1, max_height + 1):
        arr_count[i] += arr_count[i - 1]
    # i가 n -1, n - 2, ..., 0 되도록 하기 위해서
    # 길이가 n인 배열 dumps의 인덱스 최댓값은 n - 1이니까!
    for i in range(n - 1, -1 ,-1):
        arr_count[dumps[i]] -= 1
        arr_sorted[arr_count[dumps[i]]] = dumps[i]
    return arr_sorted

def swea1208():
    tc = 10
    n = 100
    max_height = 100
    for t in range(1, tc + 1):
        num_dump = int(input()) # 높이 쌓인 상자를 낮은 곳으로 옮기는 행위(dump)의 갯수
        dumps = list(map(int, input().split()))
        dumps = counting_sort(dumps, n, max_height)

        
        for _ in range(num_dump): # 정렬된 배열에 대하여 반복문이 진행되도록 한다.
            dumps[-1] -= 1 # 가장 높이 쌓인 곳에서 하나를 빼서
            dumps[0] += 1 # 가장 낮게 쌓인 곳에 쌓는다.
            dumps = counting_sort(dumps, n, max_height) # 그리고 다시 카운팅정렬을 진행한다.

        print(f"#{t} {dumps[-1] - dumps[0]}") # 정렬된 배열에서 최대값과 최소값을 뺀 값이 출력되도록 한다.
if __name__ == "__main__":
    swea1208()