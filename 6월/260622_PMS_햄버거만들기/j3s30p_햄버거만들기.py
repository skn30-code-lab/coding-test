# https://school.programmers.co.kr/learn/courses/30/lessons/133502


# 1231
def solution(ingredient):
    hamburger = [1,2,3,1]
    temp = []
    answer = 0
    for i in ingredient:
        temp.append(i)
        if len(temp) >= 4 and temp[-4:] == hamburger:
            temp[-4:] = []
            answer += 1
    return answer


a = [2, 1, 1, 2, 3, 1, 2, 3, 1] #2
b = [1, 3, 2, 1, 2, 1, 3, 1, 2] #0
print(solution(a))
print(solution(b))