def gcd(a,b,c,d):
    x=[]
    num = d*a + b*c         # 분자
    denom = b*d             # 분모 
    for i in range(1,(min(num,denom)+1)):       # 1 부터 분모분자 작은값까지
        if num % i == 0 and denom % i == 0:     # 서로 나눠서 나머지가 없을때 = 공약수
            x.append(i)
    return x
        


def solution(a,b,c,d):
    num = d*a + b*c
    denom = b*d
    return [int(num/max(gcd(a,b,c,d))),int(denom/max(gcd(a,b,c,d)))]    # max > 최대 공약수로 나눠주기