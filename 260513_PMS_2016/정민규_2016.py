def solution(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #1월1일이 금요일이므로 시작을 금요일로 설정
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    total= sum(months[0:a-1]) + (b - 1)
    answer = day[total% 7]
    return answer