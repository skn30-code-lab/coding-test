def gcd(a,b):                                   # 두 수의 최대 공약수 구하는 함수
    while b:
        a ,b = b , a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    answer = []
    r = 0
    numer = 0
    denom = 0 
    
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2
    r = gcd(numer,denom) 
    numer = numer // r
    denom = denom // r
    answer.append(numer)
    answer.append(denom)
    return answer

"""
최초 풀이 : 처음 문제를 읽고 그대로 풀때는 분자와 분모 경우의 수에 따라 if문을 통해
            케이스를 나눴지만 다시 생각해보니 결국 어떤 경우가 됐든 통분하여 더한 결과에서
            각 분자,분모를 두 수의 최대 공약수로 나누면 된다는 것을 깨달음
def gcd(a,b):                                  
    while b:
        a ,b = b , a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    answer = []
    r = 0
    numer = 0
    denom = 0 
    
    if denom1 == denom2:                   
        numer = numer1 + numer2
        if numer == denom1:
            numer = 1
            denom1 = 1
            answer.append(numer)
            answer.append(denom1)
        else:
            r = gcd(numer,denom1) 
            numer = numer // r
            denom1 = denom1 // r
            answer.append(numer)
            answer.append(denom1)
        else:
            numer = (numer1 * denom2) + (numer2 * denom1)
            denom = denom1 * denom2
            r = gcd(numer,denom) 
            numer = numer // r
            denom = denom // r
            answer.append(numer)
            answer.append(denom)
    return answer """
     