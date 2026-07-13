# https://school.programmers.co.kr/learn/courses/30/lessons/389480


#============ DP import ============
from functools import lru_cache

def solution(info, n, m):
    depth = len(info)

    @lru_cache(maxsize=None)    
    def dfs(idx, trace_a, trace_b):
        if trace_a >= n or trace_b >= m:
            return float('inf')
        if idx == depth:
            return trace_a
        
        a, b = info[idx]
        return min(
            dfs(idx + 1, trace_a + a, trace_b),
            dfs(idx + 1, trace_a, trace_b + b),
        )
    
    answer = dfs(0, 0, 0)
    return answer if answer != float('inf') else -1

#============ DP set 구현 ============
# def solution(info, n, m):
#     depth = len(info)
#     memo = {}
    
#     def dfs(idx, trace_a, trace_b):
#         if trace_a >= n or trace_b >= m:
#             return float('inf')
#         if idx == depth:
#             return trace_a
        
#         key = (idx, trace_a, trace_b)
#         if key in memo:
#             return memo[key]
        
#         a, b = info[idx]
#         result = min(
#             dfs(idx + 1, trace_a + a, trace_b),
#             dfs(idx + 1, trace_a, trace_b + b),
#         )
#         memo[key] = result
#         return result    
    
#     answer = dfs(0, 0, 0)
#     return answer if answer != float('inf') else -1

#============ DP (visited) ============
# def solution(info, n, m):
#     depth = len(info)
#     answer = float('inf')

#     visited = set()
#     def dfs(idx, trace_a, trace_b):
#         nonlocal answer
#         if trace_a >= n or trace_b >= m:
#             return
#         if idx == depth:
#             answer = min(answer, trace_a)
#             return
        
#         key = (idx, trace_a, trace_b)
#         if key in visited:
#             return
#         visited.add(key)
#         a, b = info[idx]
#         dfs(idx + 1, trace_a + a, trace_b)
#         dfs(idx + 1, trace_a, trace_b + b)
    
#     dfs(0, 0, 0)
#     return answer if answer != float('inf') else -1

if __name__ == "__main__":
    test_cases = [
        ([[1, 2], [2, 3], [2, 1]], 4, 4, 2),
        ([[1, 2], [2, 3], [2, 1]], 1, 7, 0),
        ([[3, 3], [3, 3]], 7, 1, 6),
        ([[3, 3], [3, 3]], 6, 1, -1),
    ]

    for i, (info, n, m, expected) in enumerate(test_cases, 1):
        result = solution(info, n, m)
        status = "O" if result == expected else "X"
        print(f"[{status}] test {i}: got={result}, expected={expected}")