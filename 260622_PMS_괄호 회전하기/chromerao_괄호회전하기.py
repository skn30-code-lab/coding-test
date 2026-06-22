from collections import deque
def solution(s):
    count = 0
    check = []
    que = deque(s)
    for i in range(len(que)):
        for item in que:
            if not check:
                check.append(item)
            elif check[-1] == '[' and item == ']':
                check.pop()
            elif check[-1] == '{' and item == '}':
                check.pop()
            elif check[-1] == '(' and item == ')':
                check.pop()
            else:
                check.append(item)
        if not check:
            count += 1
        else:
            check = []
        que.append(que[0])
        que.popleft()
    
    return count