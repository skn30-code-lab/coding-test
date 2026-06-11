from datetime import date
def solution(a, b):
    weekday = ['MON','TUE','WED','THU','FRI','SAT','SUN'] 
    d = date(2016,a,b) # 년,월,일 
    i = d.weekday() # 날짜 d에 해당하는 요일을 정수로 반환, 0~6, 월~일요일에 대응
    
    return  weekday[i]