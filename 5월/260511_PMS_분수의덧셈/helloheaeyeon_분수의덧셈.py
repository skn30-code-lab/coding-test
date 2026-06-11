#for 문 돌려서 나눠가면서 기약분수 만들기
def solution1(n1, d1, n2, d2):
    answer = []
    num = n1 * d2 + n2 * d1
    den = d1 * d2
    #기약분수 구하기: den 의 나눠지는 것 중 0으로 떨어지는 것
    answer = [num, den]
    #GCD는 num이나 den 보다 클 수 없다고 함, answer의 작은 값 사용
    min_num = min(answer)
    for i in range(min_num,0, -1):
        if list(map(lambda x: x%i,[num, den] )) == [0, 0]:
            return [int(x/i) for x in answer]
    return answer

#math import 해서 gcd 바로 구하기
import math
def solution2(n1, d1, n2, d2):
    answer = []
    num = n1 * d2 + n2 * d1
    den = d1 * d2
    my_gcd = math.gcd(num, den)
    answer = [num/my_gcd, den/my_gcd]
    return answer
