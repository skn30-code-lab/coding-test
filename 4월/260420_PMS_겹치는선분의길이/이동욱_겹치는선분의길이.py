def solution(lines):
    
    
    a=lines[0]              # 첫번째로 입력되는 선분 정의
    b=lines[1]              # 두번째로 입력되는 선분 정의
    c=lines[2]              # 세번째로 입력되는 선분 정의
    
    
    aa=range(a[0],a[1])     # 첫번째 선분의 길이 정의
    bb=range(b[0],b[1])     # 두번째 선분의 길이 정의   
    cc=range(c[0],c[1])     # 세번째 선분의 길이 정의 
    
    
    s1=set(aa)&set(bb)      # 첫번째 선분과 두번째 선분의 겹치는 길이 구하기 (중복제거와 동시에 교집합)
    s2=set(cc)&set(bb)      # 세번째 선분과 두번째 선분의 겹치는 길이 구하기
    s3=set(aa)&set(cc)      # 첫번째 선분과 세번째 선분의 겹치는 길이 구하기
    
    
    s4 = s1 | s2 | s3       # 각 교집합의 합집합 구하기

    
    return len(s4)          # 합집합의 길이 구하기