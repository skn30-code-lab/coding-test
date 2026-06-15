def solution(nums):
    return min(len(set(nums)), len(nums) // 2)

# 시도 1(오답)
# from itertools import permutations

# def solution(nums):
#     cases = list(permutations(nums, len(nums)//2))
#     cases = set(cases)
#     answer = len(cases)
#     return answer

# 시도 2(오답)
# from collections import Counter
# import math

# def solution(nums):

# counts = Counter(nums)
# # 1. 가장 높은 빈도수(최댓값) 파악
# max_frequency = max(counts.values())
# # 2. 최대 빈도수와 일치하는 모든 원소 추출 (리스트 컴프리헨션)
# most_common_elements = [element for element, freq in counts.items() if freq == max_frequency]
# # 3. 추출된 각 원소별로 N개를 뽑는 경우의 수 계산
# N = len(nums)//2
# for element in most_common_elements:
#     ways_to_pick = math.comb(set(nums), N)
#     print(f'{ways_to_pick}')

# 시도 3(오답)
# from itertools import permutations

# def solution(nums):
#     return len(list(permutations(set(nums), len(nums)//2))

# 다른 답안(1)
# def solution(nums):
#     max_num = len(nums)//2

#     if len(set(nums)) >= max_num:
#         return max_num
#     else:
#         return len(set(nums))

# 다른 답안(2)
# def solution(nums):
#     answer = 0
#     pocket = {}
#     check = set()
#     for i in nums:
#         pocket[i] = pocket.get(i, 0) + 1

#     for no, cnt in pocket.items():
#         if no not in check and answer < len(nums)/2:
#             check.add(no)
#             answer += 1
#     return answer
