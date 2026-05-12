def solution(list1):
    x=[]
    u=0
    num = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
    }

    while u<len(list1):     # 기본적인 아이디어 > 문자열은 3개에서 5개 사이이므로 3,4,5 탐색해서 키에 있으면 추가, 이외는 숫자니까 숫자추가
    
    # try:
    #     x.append(int(list1[u]))
    #     u+=1
    # except IndexError:
    #     pass
        if (list1[u:u+3] in num)==True:
            x.append(num.get(list1[u:u+3]))
            u+=3
            continue
        elif (list1[u:u+4] in num)==True:
            x.append(num.get(list1[u:u+4]))
            u+=4
            continue
        elif (list1[u:u+5] in num)==True:
            x.append(num.get(list1[u:u+5]))
            u+=5
            continue
        else:
            x.append(int(list1[u]))
            u+=1
    return int("".join(map(str, x)))

