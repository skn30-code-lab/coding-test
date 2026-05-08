# https://school.programmers.co.kr/learn/courses/30/lessons/120808
def gcd(a, b):
    '''
    기본 유클리드 호제법 기반 뺼셈
    '''
    while b:
        if a > b:
            a, b = b, a
        b -= a
    return a

def mod_gcd(a, b):
    '''
    gcd 기반 나머지 계산
    '''
    if not b:
        return a
    return mod_gcd(b, a % b)

def bin_gcd(a, b):
    '''
    나눗셈 계산보다 빠른 비트연산 기반
    '''
    shift = 1
    while not (a&1 or b&1):
        a >>= 1
        b >>= 1
        shift <<= 1
    while not a&1:
        a >>= 1
    
    while b:
        while not b&1:
            b >>= 1
        if a > b:
            a, b = b, a
        b -= a
    return shift * a

def solution(numer1, denom1, numer2, denom2):
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2
    g = gcd(numer, denom)
    #g = mod_gcd(numer, denom)
    #g = bin_gcd(numer, denom)
    return [numer//g, denom//g]

print(solution(1, 2, 3, 4)) # [5, 4]
print(solution(9, 2, 1, 3)) # [29, 6]
