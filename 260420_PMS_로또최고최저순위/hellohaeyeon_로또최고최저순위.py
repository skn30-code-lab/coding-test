def solution(lottos, win_nums):
    win_dic = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    zero_cnt = lottos.count(0)
    popz_lottos = [x for x in lottos if x]
    least_win_number = 0
    for num in popz_lottos:
        if num in win_nums:
            least_win_number += 1
    min_win = win_dic[least_win_number]
    max_win = win_dic[least_win_number + zero_cnt]
    answer = [max_win, min_win]
    return answer
