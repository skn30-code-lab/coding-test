def solution(s):
    answer = []
    for idx, char in enumerate(s):
        if char in s[:idx]:
            answer.append(s[(idx - 1)::-1].index(char) + 1)
        else:
            answer.append(-1)
    return answer
