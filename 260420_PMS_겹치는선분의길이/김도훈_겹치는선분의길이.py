def solution(lines):
    # 1. 모든 좌표 범위를 커버하는 리스트 생성 (인덱스를 좌표로 활용)
    # 좌표 범위가 -100 ~ 100이라면 총 200개의 칸이 필요함
    count = [0] * 200 
    
    for start, end in lines:
        # 2. 선분이 지나는 칸을 1씩 더해줌
        # 시작점부터 끝점 직전까지 1씩 표시 (선분 길이를 칸으로 계산)
        for i in range(start, end):
            count[i + 100] += 1 # 음수 좌표 처리를 위해 100을 더함
            
    # 3. 2번 이상 겹친(값이 2 이상인) 칸의 개수만 세면 정답
    answer = 0
    for c in count:
        if c >= 2:
            answer += 1
            
    return answer

# 가장 짧은 답안
# def solution(lines):
#     sets = [set(range(min(l), max(l))) for l in lines]
#     return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

# 틀린 답안
# def solution(lines):
#     ans = 0
    
#     for i in range(0,3):
#         if min(lines[i][0]) <= max(lines[i][1]):
#             result = max(lines[i][1]) - min(lines[i][0])
#             ans += result
#         else:
#             break
#     return ans