def change(num):
    if num <= 0:
        return ''
    return str(num % 3) + change(num // 3)

def solution(n):
    return int(change(n), 3)