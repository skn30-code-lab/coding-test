def change(num):
    if num <= 0:
        return ''
    char = num % 3
    num //= 3
    return str(char) + change(num)

def solution(n):
    answer = ''
    answer += change(n)
    return int(answer, 3)