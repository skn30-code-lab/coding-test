def solution(ingredient):
    answer = 0
    stack = []  # 재료 쌓을 빈 상자
    
    # 1. 재료 하나씩 꺼내 상자에 담기
    for i in ingredient:
        stack.append(i)
        
        # 2. 재료가 4개 이상 쌓였을 경우, 맨 위 4개가 햄버거 순서인지 확인
        if stack[-4:] == [1, 2, 3, 1]:
            # 3. 햄버거 순서 맞다면 포장
            answer += 1
            
            # 4. 포장한 햄버거 재료 4개 상자에서 제거
            del stack[-4:]
            
    return answer