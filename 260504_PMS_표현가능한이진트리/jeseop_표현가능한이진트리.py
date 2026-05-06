def make_full(number):          # 포화 이진트리로 만들기
    length = len(number)
    k = 0
    while (2**k  - 1) < length:
        k += 1
    k = (2**k - 1) - length

    return '0'*k + number

def check(number):               # 표현 가능한지 체크
    length = len(number)
    if length == 1:
        return 1
    length //= 2
    left = number[:length]
    right = number[length+1:]
    root = number[length]
    if root == '0' and ('1' in left or '1' in right):
        return 0

    return check(left) and check(right)

def solution(numbers):
    answer = []
    for number in numbers:
        bin_num = bin(number)[2:]                   # 이진수로 만들기
        bin_num = make_full(bin_num)                # 포화이진트리로 만들기
        answer.append(check(bin_num))               # 표현가능한지 체크하기

    return answer