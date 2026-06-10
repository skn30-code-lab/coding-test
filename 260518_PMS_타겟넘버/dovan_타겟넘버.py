# DFS
def solution(numbers, target):
    # 초기 상태: 누적합 0을 만드는 방법 1가지
    dp = {0: 1}
    
    for num in numbers:
        next_dp = {}
        for total, count in dp.items():
            # 더하는 경우의 수 누적
            next_dp[total + num] = next_dp.get(total + num, 0) + count
            # 빼는 경우의 수 누적
            next_dp[total - num] = next_dp.get(total - num, 0) + count
        dp = next_dp
        
    return dp.get(target, 0)

    
# BFS
# def solution(numbers, target):
#     leaves = [0]
    
#     for num in numbers:
#         next_leaves = []
#         for leaf in leaves:
#             next_leaves.append(leaf + num)
#             next_leaves.append(leaf - num)
#         leaves = next_leaves
        
#     return leaves.count(target)

    
# stack DFS
# def solution(numbers, target):
#     answer = 0
#     stack = [(0, 0)]  # (현재 인덱스, 누적합)
    
#     while stack:
#         idx, current_sum = stack.pop()
        
#         # 배열의 끝에 도달했을 때
#         if idx == len(numbers):
#             if current_sum == target:
#                 answer += 1
#         else:
#             # 다음 숫자를 더하는 경우와 빼는 경우를 스택에 추가
#             stack.append((idx + 1, current_sum + numbers[idx]))
#             stack.append((idx + 1, current_sum - numbers[idx]))
            
#     return answer

# 재귀 DFS
# def solution(numbers, target):
#     answer = 0
    
#     def dfs(idx, current_sum):
#         nonlocal answer
        
#         if idx == len(numbers):
#             if current_sum == target:
#                 answer += 1
#             return
            
#         dfs(idx + 1, current_sum + numbers[idx])
#         dfs(idx + 1, current_sum - numbers[idx])
        
#     dfs(0, 0)
#     return answer
