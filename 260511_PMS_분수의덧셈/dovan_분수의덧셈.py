def solution(numer1, denom1, numer2, denom2):
    
    numer=numer1 * denom2 + numer2*denom1
    denom=denom1* denom2
    
    i=[]
    for num in range(1, min(numer,denom)+1):
        if numer%num==0 and denom%num==0:
            i.append(num)
            print(i)
    gcd=max(i)
    answer=[numer/gcd, denom/gcd]
    
    return answer
