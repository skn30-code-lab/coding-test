import datetime

def solution(a, b):
    day_name_dic = { 0:"MON"
                , 1:"TUE"
                , 2:"WED"
                , 3:"THU"
                , 4:"FRI"
                , 5:"SAT"
                , 6:"SUN"}
    yy = 2016
    d = datetime.datetime(yy, a, b)
    day_num = d.weekday()
    answer = day_name_dic[day_num]
    return answer
a, b = 5, 24
ans = solution(a, b)
print(f'input\na: {a}\nb: {b}\nexcept answer:"TUE"\nanswer: {ans}')
