# 재귀 방식 시도했으나 실패(리소스/타임 문제로 보임)
# def solution(ingredient):
#     answer = 0
#     str_list = list(map(str,ingredient))
#     def count_buger(in_list):
#         nonlocal answer
#         in_str = ''.join(in_list)
#         hambuger = in_str.count('1231')
#         answer  += hambuger
#         out_list = in_str.replace('1231', '').split()
#         if hambuger == 0:
#             return
#         count_buger(out_list)
#     count_buger(str_list)
#     return answer

def solution(ingredient):
    answer = 0
    stack_list = []
    hambuger = [1, 2, 3, 1]
    for v in ingredient:
        stack_list.append(v)
        try:
            if stack_list[-4:] == hambuger:
                answer += 1
                del stack_list[-4:]
                # stack_list = stack_list[:-4]
        except:
            continue
    return answer

##########check answer##########
test_list = [([2, 1, 1, 2, 3, 1, 2, 3, 1], 2), ([1, 3, 2, 1, 2, 1, 3, 1, 2], 0)]

for ind, ans in test_list:
    print(f'ingredient: {ind}\nsolution: {solution(ind)}\nexcepted answer: {ans}')