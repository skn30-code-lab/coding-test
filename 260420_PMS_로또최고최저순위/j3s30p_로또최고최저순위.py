def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero = 0
    match = 0
    for num in lottos:
        if num == 0:
            zero += 1
        elif num in win_nums:
            match += 1
    return [rank[match + zero], rank[match]]
