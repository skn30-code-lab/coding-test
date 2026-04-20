#프로그래머스 로또 최고 및 최저순위
def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    correct = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
            correct +=1
        elif i ==0 :
            zero += 1
    answer1 = correct
    answer2 = correct+zero
    answer = [rank[answer2],rank[answer1]]
    return answer