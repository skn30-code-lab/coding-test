# https://school.programmers.co.kr/learn/courses/30/lessons/468380


# ([3, 2, 3, 1, 1], 5, 7, [8, 2]),
# 3 3 3 2 2 3 3 3 1 1
# ([2, 2, 2], 2, 2, [2, 6]),
# 2 2 2 2 2 2
    # 구간1) arr[0] = 3
    # 구간2) arr[0]+arr[1] = 5
    # if l <= 구간2x -> l = arr[1], #if r <= 구간3y -> r = arr[2]
    # 더할 것 = x-l+1 * arr[1] + (중간 arr의 값 다 더하기) +y-r+1  * arr[3]

def get_K(arr, l, r):
    curr = 0
    K = 0
    
    for i, num in enumerate(arr):
        curr += num
        index = i
        if l <= curr:
            break;
    
    # l, r이 같은 구간일 때
    if r <= curr:
        return (r - l + 1) * arr[index]

    # l 구간
    K += (curr - l + 1) * arr[index]

    # 중간구간 + r구간
    for num in arr[index + 1:]:
        index += 1
        
        if curr + num < r:
            curr += num
            K += num * num
        else:
            K += (r - curr) * num
            break
    return K

def get_C(arr, size, K):
    C = 0
    length = sum(arr) - size + 2
    for start in range(1, length):
        end = start + size - 1
        curr_K = get_K(arr, start, end)
        if curr_K == K:
            C += 1
    return C

def solution(arr, l, r):
    
    K = get_K(arr, l, r)
    size = r - l + 1
    C = get_C(arr, size, K)
    
    return [K, C]


def main():
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


if __name__ == "__main__":
    main()
