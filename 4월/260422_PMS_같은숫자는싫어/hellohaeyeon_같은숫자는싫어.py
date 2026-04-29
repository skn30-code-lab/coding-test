def solution(arr):
    cnt = 0
    answer = []
    stack = []
    for i in arr:
        cnt += 1
        if cnt == 1:
            #첫번쨰는 무조건 stack과 answer에 들어가야 함
            stack.append(i)
            answer.append(i)
            continue
        hate = stack[-1]
        if i == hate:
            continue
        else:
            answer.append(i)
            stack.append(i)
    return answer
