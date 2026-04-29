def solution(n):
    
    answer= " "                     #3진법이 거꾸로된 수를 담을 answer 문자열 생성(3진법으로 된 숫자를 담을 예정이므로 문자열로 저장)
    
    while n > 0:
        answer += str(n % 3)        #3진법 생성원리
        n //= 3                     #몫으로 while 문 돌리기
    
    return int(answer, 3)           #파이썬 내장함수: answer에 담긴 3진법수를 읽고 자동으로 10진법 수로 변환

solution(45)
solution(120)