def make_full(number):          # 포화 이진트리로 만들기
    length = len(number)
    k = 0
    while (2**k  - 1) < length:
        k += 1
    k = (2**k - 1) - length
    while k:
        number = '0' + number
        k -= 1
    return number

def check(number, length):      # 표현 가능한지 체크
    left = number[:length//2]
    right = number[(length//2)+1:]
    root = number[length // 2]

    if length == 1:
        return 1
    if root == '0' and ('1' in left or '1' in right):
        return 0
    if check(left, length//2) and check(right, length//2):
        return 1
    return 0

def solution(numbers):
    answer = []
    for number in numbers:
        bin_num = bin(number)[2:]                   # 이진수로 만들기
        bin_num = make_full(bin_num)                # 포화이진트리로 만들기
        answer.append(check(bin_num, len(bin_num))) # 표현가능한지 체크하기

    return answer