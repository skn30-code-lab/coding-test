def solution(s):
    answer = 0
    alp_list = ['zero','one','two','three','four','five','six','seven',
               'eight','nine']
    for i in range(len(alp_list)):
        if alp_list[i] in s:
            s = s.replace(alp_list[i],str(i))
    s = int(s)
    return s