def solution(number, limit, power):
    knights = [0] * (number + 1)
    for i in range (1, number + 1):
        for j in range(i, number + 1, i):
            knights[j] += 1
    knights = list(map(lambda x: power if x > limit  else x, knights))
    answer = sum(knights)
    return answer
