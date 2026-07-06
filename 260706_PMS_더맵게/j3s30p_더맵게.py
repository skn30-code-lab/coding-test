# https://school.programmers.co.kr/learn/courses/30/lessons/42626

# ===========deque popleft============
# 테스트 1 〉	통과 (74.55ms, 19.5MB)
# 테스트 2 〉	통과 (143.23ms, 27.3MB)
# 테스트 3 〉	통과 (502.01ms, 65.1MB)
# 테스트 4 〉	통과 (56.27ms, 17.9MB)
# 테스트 5 〉	통과 (519.19ms, 67.7MB)

from collections import deque
def pop_min(que1, que2):
        if not que1:
              return que2.popleft()
        if not que2:
              return que1.popleft()
        if que1[0] <= que2[0]:
              return que1.popleft()
        return que2.popleft()

def solution(scoville, K):
    count = 0
    que = deque(sorted(scoville))
    mix_que = deque()
    
    while True:
        small1 = pop_min(que, mix_que)
        if small1 >= K:
              return count
        if not que and not mix_que:
              return -1
        small2 = pop_min(que, mix_que)
        mix_que.append(small1 + small2*2)
        count += 1

# ===========import heapq============
# 테스트 1 〉	통과 (161.24ms, 17.3MB)
# 테스트 2 〉	통과 (384.13ms, 23.2MB)
# 테스트 3 〉	통과 (1577.94ms, 50.6MB)
# 테스트 4 〉	통과 (124.10ms, 16MB)
# 테스트 5 〉	통과 (1626.58ms, 52.6MB)

# from heapq import heapify, heappop, heappush
# def solution(scoville, K):
#     count = 0
#     heapify(scoville)

#     while scoville[0] < K:
#         if len(scoville) < 2:
#             return -1
        
#         small1 = heappop(scoville)
#         small2 = heappop(scoville)
#         heappush(scoville, small1 + small2*2)
#         count += 1 
#     return count

# ===========heap 직접구현============
# def sift_up(heap, i):
#     while i > 0:
#         parent = (i - 1) // 2
#         if heap[parent] <= heap[i]:
#             break
#         heap[parent], heap[i] = heap[i], heap[parent]
#         i = parent

# def heappush(heap, value):
#     heap.append(value)
#     sift_up(heap, len(heap)-1)

# def sift_down(heap, i):
#     n = len(heap)
#     while True:
#         smallest = i
#         left = i*2 +1
#         right = i*2 +2
    
#         if left < n and heap[left] < heap[smallest]:
#             smallest = left
#         if right < n and heap[right] < heap[smallest]:
#             smallest = right
#         if smallest == i:
#             break
#         heap[i], heap[smallest] = heap[smallest], heap[i]
#         i = smallest
 
# def heappop(heap):
#     result = heap[0]
#     last = heap.pop()
#     if heap:
#         heap[0] = last
#         sift_down(heap, 0)
#     return result

# def heapify(heap):
#     n = len(heap)
#     for i in range(n//2 -1, -1, -1):
#         sift_down(heap, i)


# def solution(scoville, K):
#     count = 0
#     heapify(scoville)
#     while scoville[0] < K:
#         if len(scoville) < 2:
#             return -1
#         small1 = heappop(scoville)
#         small2 = heappop(scoville)
#         heappush(scoville, small1 + small2*2)
#         count += 1
#     return count

# ===========일반 로직============
# def solution(scoville, K):
#     count = 0
#     while min(scoville) < K: 
#         if len(scoville) < 2:
#             return -1
#         small1 = scoville.pop(scoville.index(min(scoville)))
#         small2 = scoville.pop(scoville.index(min(scoville)))
#         scoville.append(small1 + small2 * 2)
#         count += 1
#     return count

scoville = [1, 2, 3, 9, 10, 12]
k =	7
OUTPUT = 2
print(f'{solution(scoville, k)}\n{OUTPUT}')