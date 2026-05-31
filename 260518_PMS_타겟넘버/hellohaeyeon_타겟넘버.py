#숫자 하나는 +와 -로 나눠짐
def plus_minus(num1, num2):
    result = []
    num2_list = [num2, -num2]
    for i in num2_list:
        r = num1 + i
        result.append(r)
    return result
        
def solution(numbers, target):
# loc_index: 현재의 계층 인덱스(depth에서 -1이 됨)
# full_depth: 마지막 계층의 깊이
    answer = 0
    full_depth = len(numbers)
    loc_index = 0
    sum_list = []
    tmp_result = []
    answer = 0
# full depth 보다 작을 때까지 while문 돌아가도록 함
# 종료 조건은 원하는 depth의 index에 도달하는 경우
# 종료시 해당 계층 모든 합의 리스트를 리턴
# 현재 방식은 DFS 보다 BFS 에 가깝다고 함
# 그리고 계층이 정해져 있기에 굳이 while 문을 사용하지 않아도 된다고 함
    while loc_index < full_depth:
        sum_list = []
        target_num = numbers[loc_index]
        if loc_index == 0:
            tmp_result = plus_minus(0, target_num)
            loc_index += 1
            continue
        else:
            for i in tmp_result:
                sum_list += plus_minus(i, target_num)
            tmp_result = sum_list
            if loc_index == full_depth - 1:
                break
        loc_index += 1
    answer = sum_list.count(target)
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
