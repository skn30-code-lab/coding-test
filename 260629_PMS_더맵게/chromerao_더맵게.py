from heapq import heapify , heappop , heappush  #  heap 모듈 불러오기
def solution(scoville, K):
    answer = 0
    heapify(scoville)                   # 기존 리스트를 heap 구조로 변환
    
    if scoville[0] >= K:
        return 0
    
    for i in range(len(scoville)-1):    # 최대 섞을 수 있는 만큼
        if scoville[0] >= K:            # 최소값이 K 이상인 경우 중단
            break
        m = scoville[0]                 # 첫 번째 최소값 저장 후 pop
        heappop(scoville)
        n = scoville[0]                 # 두 번째로 작은 값 저장 후 pop
        heappop(scoville)
        r = m + n*2                     # 섞은 값 push
        heappush(scoville,r)
        answer += 1
    if scoville[0] < K:                 # 최소값이 K 미만인 경우 -1
        return -1
        
    return answer


# 초기 작성 코드 (효율성 테스트 탈락) heap 자료구조 사용하지 않으면 시간 초과
# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
    
#     if min(scoville) >= K:
#         return 0
    
#     while min(scoville) < K:
#         scoville[1] = scoville[0] + (scoville[1] * 2)
#         scoville.pop(0)
#         answer += 1
#         scoville.sort()
        
#     if min(scoville) < K:
#         return -1
    
#     return answer