def solution(record):
    USER = {}
    LOG = []
    MESSAGE = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        log = r.split()
        if log[0] == 'Enter':
            USER[log[1]] = log[2]
            LOG.append([log[1], log[0]])
        elif log[0] == 'Leave':
            LOG.append([log[1], log[0]])
        elif log[0] == 'Change':
            USER[log[1]] = log[2]
    answer = []
    for log in LOG:
        answer.append(USER[log[0]] + MESSAGE[log[1]])
    return answer

INPUT = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
OUTPUT = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# solution(INPUT)
print(f"{solution(INPUT)}\n{OUTPUT}")