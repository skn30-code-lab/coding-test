def solution(n):
    x = []
    answer = 0
    while n > 0:
      x.append(n%3)
      n //= 3
      # 정수 나눗셈 (내림)......
      #  /=	부동소수점 나눗셈	float	5 / 3 = 1.666...
      # //=	정수 나눗셈 (내림)	int	5 // 3 = 1
    x.reverse()
    for i, digit in enumerate(x):
       answer += digit * (3**i)
    return answer



solution(45)
