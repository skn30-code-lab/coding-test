def change(num):
    if num <= 0:
        return ''
    char = num % 3
    num //= 3
    return str(char) + change(num)

def solution(n):
    return int(change(n), 3)

print(solution(45))