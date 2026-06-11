def solution(s):
    answer = s
    str_tuple = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero')
    num_tuple = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    str_dic = dict(zip(str_tuple, num_tuple))
    for k, v in str_dic.items():
        try:
            answer = answer.replace(k,v)
        except:
            continue
    answer = int(answer)
    return answer
in_str = "one4seveneight"
except_ans = 1478
ans = solution(in_str)
print(f'input: {in_str}\nexcept: {except_ans}\nanswer: {ans}')
