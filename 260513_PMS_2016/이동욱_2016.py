def solution(a,b):
    day = {
    0: "SAT",
    1: "SUN",
    2: "MON",
    3: "TUE",
    4: "WED",
    5: "THU",
    6: "FRI"
    }
    dic = {
    1:1,
    2:4,
    3:4,
    4:0,
    5:2,
    6:5,
    7:0,
    8:3,
    9:6,
    10:1,
    11:4,
    12:6
    }
    if a == 1 or a == 2 :
        return day.get((25+dic.get(a)+b)%7)
    else:
        return day.get((26+dic.get(a)+b)%7)
    
    # 참고 블로그 https://m.blog.naver.com/yhc33758/222922768282