def solution(s, n):
    answer = ''
    
    # 딕셔너리 대신 문자열 인덱스(0~25)를 사용하여 매핑 구조를 대체
    lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
    upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for char in s:
        if char in lower_alpha:
            # 현재 문자의 인덱스를 찾고 n을 더한 뒤 26으로 나눈 나머지로 순환
            new_idx = (lower_alpha.index(char) + n) % 26
            answer += lower_alpha[new_idx]
        elif char in upper_alpha:
            new_idx = (upper_alpha.index(char) + n) % 26
            answer += upper_alpha[new_idx]
        else:
            answer += char  # 공백인 경우 그대로 추가
            
    return answer

# def caesar(s, n):
#     s = list(s)
#     for i in range(len(s)):
#         if s[i].isupper():
#             s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
#         elif s[i].islower():
#             s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

#     return "".join(s)
