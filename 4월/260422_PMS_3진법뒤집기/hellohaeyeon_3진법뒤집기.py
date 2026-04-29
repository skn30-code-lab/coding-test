def solution(n):
    tmp_str = ""
    # convert Ternary
    while n >= 3:
        d, m = divmod(n, 3)
        m = str(m)
        tmp_str += m
        n = d
    # 이것 자체가 뒤집은 것이나, 계산을 위해선 reverse 필요
    tmp_str += str(n)
    cnt = 0
    result = 0
    if len(tmp_str) > 1:
        tmp_str = tmp_str[::-1]
        for x in tmp_str:
            tmp_int = (3**cnt) * int(x)
            result += tmp_int
            cnt += 1
    else:
        result = int(n)
    return result
