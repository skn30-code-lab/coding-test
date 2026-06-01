#재귀를 활요한 DFS 구현
def solution(numbers, target):
    answer = 0
    #상태: (index, 합)
    def dfs(index, total):
        #len(numbers)를 n 이라고 하면
        #index는 0, 1, 2, 3, 4... 마지막 인덱스는 n-1
        #index 변수가 n에 도달하는 경우: numbers 순회를 마친 경우
        # 함수에서 정의된 answer를 가져옴
        nonlocal answer
        # number를 모두 순회한 경우 그 합(total)을 target과 비교하고 함수 종료
        if index == len(numbers):
            if total == target:
                answer += 1
            return
        dfs(index + 1, total + numbers[index])
        dfs(index + 1, total - numbers[index])
    # 재귀로 function call
    dfs(0, 0)
    return answer
##########print answer##########
test_cases = [
    ([1, 1, 1, 1, 1], 3, 5),
    ([4, 1, 2, 1], 4, 2),
]

for numbers, target, expected in test_cases:
    result = solution(numbers, target)

    print("예시 input")
    print(f"numbers = {numbers}, target = {target}")
    print(f"예상 결과: {expected}")
    print(f"실제 결과: {result}")
    print(f"정답 여부: {expected == result}")
    print("-" * 40)