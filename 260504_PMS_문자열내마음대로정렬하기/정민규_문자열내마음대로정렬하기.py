def solution(strings, n):
    answer = []
    temp = []
    for s in strings:
        temp.append(s[n] + s)

    temp.sort()
    
    for t in temp:
        answer.append(t[1:])
        
    return answer