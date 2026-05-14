LOWER = 'abcdefghijklmnopqrstuvwxyz'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ':
            answer += ' '
        elif c in UPPER:
            idx = (UPPER.index(c) + n) % len(UPPER)
            answer += UPPER[idx]
        elif c in LOWER:
            idx = (LOWER.index(c) + n) % len(LOWER)
            answer += LOWER[idx]
        # else:
        #     answer += c
    return answer

s = ['AB', 'z', 'a B z']
n = [1, 1, 4]

print(solution(s[0], n[0])) # "BC"
print(solution(s[1], n[1])) # "a"
print(solution(s[2], n[2])) # "e F d"