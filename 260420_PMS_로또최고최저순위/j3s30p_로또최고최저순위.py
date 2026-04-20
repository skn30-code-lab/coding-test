def solution(lottos, win_nums):
    rate = 6
    flag = False
    zero = 0
    for num in lottos:
        if num == 0:
            zero += 1
        if num in win_nums:
            if flag:
                rate -= 1
            flag = True

    return [1 if zero == 6 else rate - zero, rate]
