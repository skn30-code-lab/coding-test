def solution(lottos, win_nums):
    win_count = 0
    unknown_count = 0

    winning_rank = {6:1, 5:2, 4:3, 3:4, 2: 5}
    for lotto in lottos:
        if (lotto == 0):
            unknown_count += 1
        for win in win_nums:
                    # print(win, lotto)
            if (win == lotto):
                win_count += 1

    answer = [winning_rank.get(win_count+unknown_count, 6), winning_rank.get(win_count, 6)]
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
solution(lottos, win_nums)
