def solution(lines):

    end_list = [set(), set(), set()]

    for i, line in enumerate(lines):
        for x in range(line[0]+1, line[1]+1):
            end_list[i].add(x)

    duplicated = (end_list[0] & end_list[1]) | (end_list[1] & end_list[2]) | (end_list[0] & end_list[2])
    answer = len(duplicated)

    return answer

print(solution([[0, 1], [2, 5], [3, 9]]))   # 2
print(solution([[-1, 1], [1, 3], [3, 9]]))  # 0
print(solution([[0, 5], [3, 9], [1, 10]]))  # 8
