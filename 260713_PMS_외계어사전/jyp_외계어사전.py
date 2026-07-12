# 요구사항
# ["p", "o", "s"]	["sod", "eocd", "qixm", "adio", "soo"]	2
# ["z", "d", "x"]	["def", "dww", "dzx", "loveaw"]	1

# 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2

# 풀이 코드
def solution(spell, dic):
    
    for i in dic:
        if sorted(spell) == sorted(i):
            return 1
            
    return 2

# 테스트 케이스
# solution(["s", "o", "m", "d"],["moos", "dzx", "smm", "sunmmo", "som"])
# solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"])
# solution(["z", "d", "x"],["def", "dww", "dzx", "loveaw"])

# 프로그래머스 다른 사람 코드 (1) - set 사용
def solution1(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2

# set은 중복을 없애므로, 알파벳의 개수까지 비교해야 할 때는 주의

# 프로그래머스 다른 사람 코드 (2) - any 사용
def solution2(spell, dic):
    spell = set(spell)
    return int(any(d for d in dic if not spell - set(d))) or 2

# any()는 **여러 조건 중 하나라도 참이면 True**를 반환하는 함수이다.