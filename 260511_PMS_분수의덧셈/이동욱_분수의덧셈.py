def gcd(a,b,c,d):
    x=[]
    num = d*a + b*c
    denom = b*d
    for i in range(1,(min(num,denom)+1)):
        if num % i == 0 and denom % i == 0:
            x.append(i)
    return x
        


def solution(a,b,c,d):
    num = d*a + b*c
    denom = b*d
    return [int(num/max(gcd(a,b,c,d))),int(denom/max(gcd(a,b,c,d)))]