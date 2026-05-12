def solution(a, b):
    passed_days = date_check(a,b)
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']

    # 7일마다 요일이 반복되므로 나머지로 요일 찾기
    week_idx = passed_days % 7
    answer = days[week_idx]
    
    return answer

def date_check(m,d):
    month = m - 1
    date = d - 1 
    month_days = [31,29,31,30,31,30,31,31,30,31,30,31]
    tmp = month_days [:month]

    return sum(tmp) + date

solution(1, 2)
solution(5, 24)
