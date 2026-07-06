def solution(scoville, K):
    answer = 0
    scoville.sort()
    for i in range(len(scoville)):
        scoville.append(scoville[0]+scoville[1]*2)
        scoville.sort()
        scoville.pop(0)
        scoville.pop(0)
        answer+=1
        if all(x > K for x in scoville):
            break
    return answer
