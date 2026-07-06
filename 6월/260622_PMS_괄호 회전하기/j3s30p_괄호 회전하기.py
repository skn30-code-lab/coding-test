# https://school.programmers.co.kr/learn/courses/30/lessons/76502


def solution(s):
    def is_valid():
        stack = []
        pair = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack or stack[-1] != pair[c]:
                    return False
                else:
                    stack.pop()
        return not stack
    
    x = len(s)
    answer = 0
    
    for _ in range(x):
        answer += is_valid()
        
        temp = s[0]
        s = s[1:]
        s += temp
    return answer


s_list = ["[](){}", "}]()[{", "[)(]", "}}}"]
# 3, 2, 0, 0
for s in s_list:
    print(solution(s))
