def solution(s, n):
    answer = ''
    for item in s:
        if item.isupper():
            answer += chr((ord(item) - ord('A') + n) % 26 + ord('A'))
        elif item.islower():
            answer += chr((ord(item) - ord('a') + n) % 26 + ord('a'))
        else:
            answer += item  # 공백은 그대로
    
    return answer

"""
ord 안쓰는 풀이

def solution(s, n):
    answer = ''
    
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    
    for item in s:
        if item in upper:
            alp = upper.index(item)
            answer += upper[(alp + n) % 26]
            
        elif item in lower:
            alp = lower.index(item)
            answer += lower[(alp + n) % 26]
            
        else:
            answer += item
    
    return answer
"""