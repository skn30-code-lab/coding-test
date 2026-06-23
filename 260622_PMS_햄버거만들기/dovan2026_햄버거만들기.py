def solution(ingredient):
    answer = 0
    stack_list = []
    hamburger = [1, 2, 3, 1]
    
    for v in ingredient:
        stack_list.append(v)
        
        # 스택의 맨 위(가장 최근에 추가된 4개의 재료)를 확인
        if stack_list[-4:] == hamburger:
            answer += 1
            # 햄버거가 완성되었다면 해당 재료 4개를 스택에서 제거
            del stack_list[-4:]
            
    return answer

# def solution(ingredient):
#     answer = 0
#     stack = []
    
#     for v in ingredient:
#         stack.append(v)
        
#         if stack[-4:] == [1, 2, 3, 1]:
#             answer += 1
#             # 슬라이싱 삭제 대신 pop을 4번 수행
#             for _ in range(4):
#                 stack.pop()
                
#     return answer

# def solution(ingredient):
#     answer = 0
#     stack = []
    
#     for v in ingredient:
#         stack.append(v)
        
#         if stack[-4:] == [1, 2, 3, 1]:
#             answer += 1
#             # 슬라이싱 삭제
#             del stack[-4:]
                
#     return answer

# def solution(ingredient):
#     answer = 0
#     idx = 0  # 현재 값이 쌓일 위치를 가리키는 포인터
    
#     for v in ingredient:
#         # 현재 포인터 위치에 값을 덮어씌움
#         ingredient[idx] = v
#         idx += 1
        
#         # 포인터 앞의 4개가 햄버거 패턴인지 확인
#         if idx >= 4 and ingredient[idx-4:idx] == [1, 2, 3, 1]:
#             answer += 1
#             # 햄버거가 완성되면 포인터를 4칸 앞으로 되돌림 (사실상 삭제 효과)
#             idx -= 4
            
#     return answer
