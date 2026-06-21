# s = "[](){}"
# N = len(s)

def solution(s):
    s_len = len(s)          # s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시킨다 했으므로 전체길이
    count=0
    for x in range(s_len):
        
        
        a = [] 
        
        
        for i in range(s_len):
            
            t = s[(x + i) % s_len]
            
            if t in ['[', '(', '{']:
                a.append(t)             # '[', '(', '{' 얘네들을 미리 a에 추가해서 대기 시켜둠
            
        
            elif t == ']':              # 하나씩 비교해서 짝이되면 대기시켰던 괄호들 중 매칭되는 애들 pop
                if a and a[-1] == '[': 
                    a.pop()
            elif t == ')':
                if a and a[-1] == '(':
                    a.pop()
            elif t == '}':
                if a and a[-1] == '{':
                    a.pop()
        if not ('[' in s or '(' in s or '{' in s):      # 주어진 문자열 s안에 쟤네들 없으면 무조건 pop 안되므로 break
            break
        
        elif not a:                     # a안에 아무것도 없으면 모두 pop돼서 사라졌으므로 정상적인 집합들임
            count+=1

    return count
