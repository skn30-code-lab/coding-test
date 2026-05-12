WEEKS = ['SUN','MON','TUE','WED','THU','FRI','SAT']
DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
START_MONTH, START_DAY, START_WEEK = 1, 1, 'FRI'

def solution(a, b):
    month = a - START_MONTH
    day = b - START_DAY
    today = sum(DAYS[:month]) + day + WEEKS.index(START_WEEK)
    return  WEEKS[today % 7]

a=5
b=24
print(solution(a, b)) #'TUE