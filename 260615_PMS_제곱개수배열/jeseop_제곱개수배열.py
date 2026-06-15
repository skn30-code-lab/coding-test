# https://school.programmers.co.kr/learn/courses/30/lessons/468380


def get_K(arr, brr_l, brr_r):

    def get_index(loc):
        block_end = 0
        for index, num in enumerate(arr):
            block_end += num
            if loc <= block_end:
                return index
    
    K = 0

    arr_l = get_index(brr_l)
    arr_r = get_index(brr_r)
    if arr_l == arr_r:
        return (brr_r - brr_l + 1) * arr[arr_l]
    
    # l 블록
    brr_l_block_end = sum(arr[:arr_l + 1])
    K += (brr_l_block_end - brr_l + 1) * arr[arr_l]

    # 중간 블록
    brr_i = brr_l_block_end   # 현재 위치
    for i in range(arr_l + 1, arr_r):
        K += arr[i] * arr[i]
        brr_i += arr[i]

    # r 블록
    K += (brr_r - (brr_i+1) + 1) * arr[arr_r]
    
    return K

# def get_C(arr, size, K):
#     C = 0
#     length = sum(arr) - size + 2

#     for start in range(1, length):
#         end = start + size - 1
#         curr_K = get_K(arr, start, end)
#         if curr_K == K:
#             C += 1

#     return C

def get_C(arr, size, K):
    blocks = [0]
    
    for num in arr:
        blocks.append(blocks[-1] + num)
    brr_length = blocks[-1]

    C = 0
    curr_K = get_K(arr, 1, size)
    if curr_K == K:
        C += 1

    start = 1
    end = start + size

    start_block = 0         # start가 속한 블록
    end_block  = 0          # end가 속한 블록
    while end -1 < brr_length:
        
        while start > blocks[start_block + 1]:
            start_block += 1
        while end > blocks[end_block + 1]:
            end_block += 1

        delta = arr[end_block] - arr[start_block]

        start_limit = blocks[start_block + 1] - start
        end_limit  = blocks[end_block + 1] - end
        can_jump = max(min(start_limit, end_limit), 1)

        if delta == 0:
            if curr_K == K:
                C += can_jump
        else:
            diff = K - curr_K
            if diff % delta == 0:
                k = diff // delta
                if 1 <= k <= can_jump:
                    C += 1

        curr_K += can_jump * delta
        start += can_jump
        end = start + size
    return C

def solution(arr, l, r):
    K = get_K(arr, l, r)
    size = r - l + 1
    C = get_C(arr, size, K)
    
    return [K, C]



import time

test_cases = [
    # (arr, l, r, expected)
    ([3, 2, 3, 1, 1], 5, 7, [8, 2]),
    ([2, 2, 2], 2, 2, [2, 6]),
    ([8, 8, 6, 5, 2, 9, 8, 4, 3, 10], 25, 27, [15, 3]),
    ([70195, 25471, 7389, 58187, 18454, 90532, 97667, 17148, 91636, 2810],
        126058, 462933, [27554327568, 1]),
    ([16952, 70276, 16771, 37992, 87549, 54906, 36718, 20478, 57088, 27916,
        51509, 83422, 51707, 18807, 80859, 2673, 37734, 93380],
        149845, 228204, [6860339640, 9190]),
    ([49134, 86806, 94548, 88849, 95022, 28334, 16637, 79487, 23773, 7314,
        47370, 50269, 36573, 9415, 44674, 28096],
        61242, 88535, [2369282964, 59513]),
]

GREEN = "\033[92m"
RED = "\033[91m"
GRAY = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"

passed = 0
for i, (arr, l, r, expected) in enumerate(test_cases, 1):
    start = time.perf_counter()
    result = solution(arr, l, r)
    elapsed = (time.perf_counter() - start) * 1000  # ms
    if result == expected:
        passed += 1
        print(f"{GREEN}{BOLD}✔ {RESET} {GRAY}case {i}{RESET}  →  {result}  "
                f"{GRAY}🕒 {elapsed:.3f}ms{RESET}")
    else:
        print(f"{RED}{BOLD}✘ {RESET} {GRAY}case {i}{RESET}  →  "
                f"got={RED}{result}{RESET}  expected={GREEN}{expected}{RESET}  "
                f"{GRAY}🕒 {elapsed:.3f}ms{RESET}")

total = len(test_cases)
color = GREEN if passed == total else RED
print(f"\n{color}{BOLD}{passed}/{total} 통과{RESET}")