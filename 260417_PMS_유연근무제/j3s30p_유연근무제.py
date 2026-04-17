def solution(schedules, timelogs, startday):
    weekend = {(6-startday)%7, (7-startday)%7}
    answer = len(schedules)
    
    for schedule, logs in zip(schedules, timelogs):
        deadline = (schedule // 100)*60 + schedule % 100 + 10

        for idx, log in enumerate(logs):
            if idx in weekend:
                continue
            
            log = (log // 100)*60 + log % 100
            if log > deadline:
                answer -= 1
                break
    return answer