def dfs(b, left, right):                  # 표현 가능한지 체크하는 재귀함수
    if left == right:
        return True  
    
    mid = (left + right) // 2
    if b[mid] == '0':
        if '1' in b[left:right+1]:        # 구간 안에 1이 있으면 표현 불가능
            return False
        else:
            return True

    else:
        return dfs(b, left, mid - 1) and dfs(b, mid + 1, right)
        
        

def solution(numbers):
    answer = []
    for num in numbers:
        b = bin(num)[2:]
        n = len(b) + 1
        size = 1
        while size < n:
            size *= 2
        dummies = size - 1 - len(b)
        b = '0' * dummies + b            # b를 포화이진트리로 만들기
        if dfs(b,0,len(b)-1):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer