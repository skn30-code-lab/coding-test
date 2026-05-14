import string       # 알파벳 불러오기
def solution(s,b):
    x=[]
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    # lower_index = lower.index('a')
    # upper_index = upper.index('A')
    for i in s:
        if i in lower:
            lower_index = lower.index(i)
            x.append(lower[(lower_index+b)%26])
        
        elif i in upper:
            upper_index = upper.index(i)
            x.append(upper[(upper_index+b)%26])
        else:
            x.append(' ')
    return ''.join(x)
