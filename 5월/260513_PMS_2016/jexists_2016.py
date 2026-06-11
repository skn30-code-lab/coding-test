def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU',]
    # print(len(days))

    remain_days = 0
    for x in range(a):
        if (a-1) != x:
          remain_days += days[x]
          # print(days[x])
        else:
          remain_days += b
          # print(b)


    answer = week[(remain_days % 7)-1]
    return answer

# 2016 / 1 / 1 / 금
solution(5,24)	# "TUE"
