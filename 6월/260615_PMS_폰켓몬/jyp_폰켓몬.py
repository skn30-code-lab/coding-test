# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = len(nums)//2
    if answer >= len(set(nums)):
        answer = len(set(nums))
    print(answer)

# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))


    