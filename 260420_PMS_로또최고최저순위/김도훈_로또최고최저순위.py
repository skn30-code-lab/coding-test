def solution(lottos, win_nums):
    # 1. 확실히 맞은 개수 찾기 (교집합 활용)
    match_count = len(set(lottos) & set(win_nums))
    
    # 2. 모르는 번호(0)의 개수 세기
    zero_count = lottos.count(0)
    
    # 3. 순위 테이블 정의 (맞은 개수를 인덱스로 활용)
    # 6개 맞으면 1등, 5개 2등, ..., 0개나 1개는 6등
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    # 4. 최고 순위와 최저 순위 계산
    # 최고: 0이 다 맞았다고 가정 (match + zero)
    # 최저: 0이 다 틀렸다고 가정 (match)
    high = rank[match_count + zero_count]
    low = rank[match_count]
    
    return [high, low]

# 틀린 오답
# def solution(lottos, win_nums):
#     answer = []
    
#     for i in range(1,7):
#         if i == len(set(lottos) & set(win_nums)):
#             answer += 7 - i
#             if 7 - i = 1 or 0:
#                 pass
#         else:
#             pass
#     if 0 in lottos:
#         ans = lottos.count(0)
#         answer += 7 - len(set(lottos) & set(win_nums)) - ans
#     else:
#         pass
                
#     return answer


# 모범 답안
# def solution(lottos, win_nums):

#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]

