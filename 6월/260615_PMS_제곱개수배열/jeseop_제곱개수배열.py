# https://school.programmers.co.kr/learn/courses/30/lessons/468380


def get_K(arr, start, end, blocks):
    def get_index(loc):
        """brr의 index를 받아 arr의 index로 변경"""
        for index in range(len(arr)):
            if loc <= blocks[index + 1]:
                return index

    K = 0

    start_block = get_index(start)	# brr의 index인 start를 arr의 index로 변경
    end_block = get_index(end)  	# brr의 index인 end를 arr의 index로 변경

    if start_block == end_block:
        return (end - start + 1) * arr[start_block]

    # blocks는 brr에서 각 블록의 누적 끝 위치를 저장한다.
    # arr[i] 블록의 시작 위치 = blocks[i] + 1
    # arr[i] 블록의 끝 위치   = blocks[i + 1]

    # l 블록
    # blocks[i+1](끝위치) 에서 - 시작위치를 뺴고 +1
    K += (blocks[start_block + 1] - start + 1) * arr[start_block]

    # 중간 블록
    # start_block 다음부터 end_block 전까지의 중간블록
    for i in range(start_block + 1, end_block):
        K += arr[i] * arr[i]

    # r 블록
    # 끝위치에서 blcoks[i]+1(시작위치)를 빼고 +1
    K += (end - (blocks[end_block] + 1) + 1) * arr[end_block]

    # [    [왼쪽블록]] + [[    가운데블록    ]] + [[오른쪽블록]    ]
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

def get_C(arr, size, K, blocks):
    brr_length = blocks[-1]
    C = 0

    curr_K = get_K(arr, 1, size, blocks)    # 첫번째 size 구간에서 K값을 구해둠.
    if curr_K == K:
        C += 1

    # blocks가 [0, a, b, c] 순이기에 start=1부터 시작
    # 현재 size 구간은 [start, end - 1]
    start = 1
    end = start + size

    start_block = 0     # start가 속할 블록
    end_block = 0       # end가 속할 블록

    while end <= brr_length:     # end가 brr 길이를 벗어나지 않아야함
        
        while start > blocks[start_block + 1]:  # start_block(start가 속한 arr 인덱스)
            start_block += 1
        while end > blocks[end_block + 1]:      # end_block(end가 속한 arr 인덱스)
            end_block += 1

        # start, end를 한칸 오른쪽으로 밀었을 때의 변화량.
        # 빠지는 값 = arr[start_block], 들어오는 값 = arr[end_block]
        delta = arr[end_block] - arr[start_block]

        start_limit = blocks[start_block + 1] - start   # start가 block에서 벗어나지 않고 최대로 움직일 수 있는 거리
        end_limit = blocks[end_block + 1] - end         # end가 block에서 벗어나지 않고 최대로 움직일 수 있는 거리
        can_jump = max(min(start_limit, end_limit), 1)  # 그중에서 최소값만큼 이동가능하고, 0일때는 무한루프에 빠지므로 최소 한칸은 이동.

        if delta == 0:
            if curr_K == K:
                C += can_jump
        else:
            diff = K - curr_K           # 구해야하는 K와 현재 K의 차이를 구함
            if diff % delta == 0:       # 그 값이 변화량의 배수라면, 변화량 사이에 한 지점에 존재함.
                k = diff // delta       # 몇번의 변화량을 거쳐야 하는지 체크
                if 1 <= k <= can_jump:  # 그게 jump번의 반복안에 존재하는지 체크
                    C += 1

        curr_K += can_jump * delta      # 변화량에 따라 커지거나 작아짐
        start += can_jump               # jump만큼 건너뛴 start
        end = start + size              # jump만큼 건너뛴 end

    return C


def solution(arr, l, r):
    def make_blocks(arr):
        """brr의 구간 시작 index가 담긴 list"""
        blocks = [0]
        for num in arr:
            blocks.append(blocks[-1] + num)
        return blocks

    blocks = make_blocks(arr)
    K = get_K(arr, l, r, blocks)
    size = r - l + 1
    C = get_C(arr, size, K, blocks)

    return [K, C]



import time

test_cases = [
    # (arr, l, r, expected)
    ([3, 2, 3, 1, 1], 5, 7, [8, 2]),
    ([2, 2, 2], 2, 2, [2, 6]),
    ([8, 8, 6, 5, 2, 9, 8, 4, 3, 10], 25, 27, [15, 3]),
    (
        [70195, 25471, 7389, 58187, 18454, 90532, 97667, 17148, 91636, 2810],
        126058,
        462933,
        [27554327568, 1],
    ),
    (
        [
            16952,
            70276,
            16771,
            37992,
            87549,
            54906,
            36718,
            20478,
            57088,
            27916,
            51509,
            83422,
            51707,
            18807,
            80859,
            2673,
            37734,
            93380,
        ],
        149845,
        228204,
        [6860339640, 9190],
    ),
    (
        [
            49134,
            86806,
            94548,
            88849,
            95022,
            28334,
            16637,
            79487,
            23773,
            7314,
            47370,
            50269,
            36573,
            9415,
            44674,
            28096,
        ],
        61242,
        88535,
        [2369282964, 59513],
    ),
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
