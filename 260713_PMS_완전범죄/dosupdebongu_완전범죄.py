def solution(info, n, m):
    # 이미 계산한 상태와 그 결과를 저장하는 딕셔너리입니다.
    # 이것이 DP 역할을 합니다.
    memo = {}
    # index: 현재 처리할 물건 번호
    # a_sum: 지금까지 쌓인 A의 흔적
    # b_sum: 지금까지 쌓인 B의 흔적
    def dfs(index, a_sum, b_sum):
        # A의 흔적이 n 이상이면 A가 경찰에게 잡힙니다.
        # 현재 방법은 실패했으므로 None을 반환합니다.
        if a_sum >= n:
            return None
        # B의 흔적이 m 이상이면 B가 경찰에게 잡힙니다.
        # 현재 방법은 실패했으므로 None을 반환합니다.
        if b_sum >= m:
            return None

        # index가 물건 개수와 같다면
        # 모든 물건을 성공적으로 처리했다는 뜻입니다.
        if index == len(info):

            # 성공한 경우 현재까지 쌓인 A 흔적을 반환합니다.
            return a_sum

        # 현재 상태를 튜플로 만듭니다.
        # 예: (현재 물건 번호, A 흔적, B 흔적)
        state = (index, a_sum, b_sum)

        # 현재 상태를 이전에 이미 계산했다면
        if state in memo:

            # 다시 탐색하지 않고 저장된 결과를 반환합니다.
            return memo[state]

        # 현재 물건을 A가 훔치는 경우를 탐색합니다.
        result_a = dfs(
            # 현재 물건을 처리했으므로 다음 물건으로 이동합니다.
            index + 1,

            # A가 훔쳤으므로 A 흔적을 증가시킵니다.
            a_sum + info[index][0],

            # B 흔적은 그대로 유지합니다.
            b_sum
        )

        # 현재 물건을 B가 훔치는 경우를 탐색합니다.
        result_b = dfs(
            # 현재 물건을 처리했으므로 다음 물건으로 이동합니다.
            index + 1,

            # A 흔적은 그대로 유지합니다.
            a_sum,

            # B가 훔쳤으므로 B 흔적을 증가시킵니다.
            b_sum + info[index][1]
        )

        # A와 B 경로가 모두 실패한 경우입니다.
        if result_a is None and result_b is None:

            # 현재 상태에서는 성공할 방법이 없습니다.
            result = None

        # A가 훔치는 경로만 실패한 경우입니다.
        elif result_a is None:

            # B가 훔치는 경로의 결과를 사용합니다.
            result = result_b

        # B가 훔치는 경로만 실패한 경우입니다.
        elif result_b is None:

            # A가 훔치는 경로의 결과를 사용합니다.
            result = result_a

        # 두 경로 모두 성공한 경우입니다.
        else:

            # A 흔적이 더 작은 결과를 선택합니다.
            result = min(result_a, result_b)

        # 현재 상태에서 얻은 최종 결과를 저장합니다.
        # 나중에 같은 상태가 나오면 이 값을 재사용합니다.
        memo[state] = result

        # 현재 상태의 결과를 이전 DFS 호출로 반환합니다.
        return result

    # 첫 번째 물건부터 탐색합니다.
    # 처음에는 A와 B의 흔적이 모두 0입니다.
    answer = dfs(0, 0, 0)

    # 모든 방법이 실패했다면 answer는 None입니다.
    if answer is None:

        # 문제 조건에 따라 -1을 반환합니다.
        return -1

    # 성공했다면 A 흔적의 최솟값을 반환합니다.
    return answer


'''
def solution(info, n, m):

    def dfs(index, a_sum, b_sum):
        # A나 B가 잡히면 실패
        if a_sum >= n or b_sum >= m:
            return None

        # 모든 물건을 처리했다면
        # 현재 A 흔적을 결과로 반환
        if index == len(info):
            return a_sum

        # 현재 물건을 A가 훔쳤을 때의 결과
        result_a = dfs(
            index + 1,
            a_sum + info[index][0],
            b_sum
        )

        # 현재 물건을 B가 훔쳤을 때의 결과
        result_b = dfs(
            index + 1,
            a_sum,
            b_sum + info[index][1]
        )

        # A가 훔치는 방법이 실패했다면
        if result_a is None:
            return result_b

        # B가 훔치는 방법이 실패했다면
        if result_b is None:
            return result_a

        # 두 방법 모두 성공했다면 더 작은 A 흔적 반환
        return min(result_a, result_b)

    answer = dfs(0, 0, 0)

    # 성공한 방법이 없으면 -1
    if answer is None:
        return -1

    return answer
'''

#   =================================================================
# def solution(info, n, m):
#     answer = 0
#     info.sort(key=lambda x: x[0]/x[1], reverse=True)
#     print(info)

#     a_count = 0
#     b_count = 0

#     for i in info:
#         if b_count + i[1] < m:
#             b_count += i[1]
#         elif a_count + i[0] < n:
#             a_count += i[0]
#         else :
#             a_count = -1
#             break

#     return a_count