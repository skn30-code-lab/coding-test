#암호 해독판
my_str = 'abcdefghijklmnopqrstuvwxyz'
#문자 하나를 튜플 형태로 변경(인덱스, 대소문자 여부)
#' ' 인 경우는 (-1,-1)
def incode(s, in_str = my_str):
    result = (-1, -1) # space
    low_s = s.lower()
    c = s
    lc = s.lower()
    if c == ' ':
        return result
    elif c != ' ':
        x = in_str.index(lc)
        if c.isupper():
            y = 1
        else:
            y = 0
    result = (x, y)
    return result
#튜플 해독 함수, 공백확인 - 문자 변경 - 대소문자 변경
def decode(in_tuple , in_str = my_str):
    result = ' '
    x, y = in_tuple
    if in_tuple == (-1, -1):
        return result
    elif in_tuple:
        tmp = in_str[x]
        if y == 1:
            tmp = tmp.upper()
    result = tmp
    return result
#인덱스 넘어가는 애들 처리용 함수
def tuple_cut(in_tuple, in_str = my_str):
    x, y = in_tuple
    x = x % len(in_str)
    return (x, y)
def solution(s, n):
    answer = ''
    for c in s:
        incode(c)
        tmp = incode(c)
        if not tmp == (-1,-1):
            new_tuple = (tmp[0]+n, tmp[1])
            tmp = tuple_cut(new_tuple)
        tmp = decode(tmp)
        answer += tmp
    return answer
q1= ("AB", 1, "BC" )
q2 = ("z", 1, "a")
q3 = ("a B z", 4, "e F d")
qlist = (q1,q2,q3)
##check answer
for i in range(3) :
    x,y,z = qlist[i]
    print('='*10)
    print(f'q{i+1}\ninput:{x, y}\nexpect answer:{z}\nanswer:{solution(x,y)}')
