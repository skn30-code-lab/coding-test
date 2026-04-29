def solution(lottos, win_nums):
    tmp = []
    lo_cnt = lottos.count(0)
    
    for i in lottos:
        if i in win_nums:
            tmp.append(i)
    
    lotto_max = len(tmp) + lo_cnt
    lotto_min = len(tmp)

    # print(get_rank(lotto_max), get_rank(lotto_min))
    answer = get_rank(lotto_max), get_rank(lotto_min)
    return answer

# ~개 맞으면 %등
def get_rank(n):
    if n == 6: return 1
    elif n == 5: return 2
    elif n == 4: return 3
    elif n == 3: return 4
    elif n == 2: return 5
    else: return 6

solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25])
solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35])
