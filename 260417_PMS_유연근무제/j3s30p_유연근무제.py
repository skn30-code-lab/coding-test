def solution(schedules, timelogs, startday):
    remove_day = {1:(6, 5), 2:(5, 4), 3:(4, 3), 4:(3, 2), 5:(2, 1), 6:(1, 0), 7: (6, 0)}
    answer = len(schedules)
    
    for time in timelogs:
        for day in remove_day[startday]:
            time.pop(day)
    for schedule, logs in zip(schedules, timelogs):
        schedule = (schedule // 100)*60 + schedule % 100
        for log in logs:
            log = (log // 100)*60 + log % 100
            if log > schedule + 10:
                print(log, schedule)
                answer -= 1
                break;
    return answer

