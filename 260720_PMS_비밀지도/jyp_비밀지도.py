def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        # 1. 같은 위치의 숫자를 OR 연산
        merged = arr1[i] | arr2[i]

        # 2. 길이가 n인 이진수 문자열로 변환
        binary = bin(merged)[2:].zfill(n)

        # 3. 1은 #, 0은 공백으로 변환
        map_string = ''

        for number in binary:
            if number == '1':
                map_string += '#'
            else:
                map_string += ' '

        # 4. 완성된 지도 한 줄을 answer에 추가
        answer.append(map_string)

    return answer

# 프로그래머스 다른 풀이
# zip(arr1, arr2) -> 배열의 같은 위치에 있는 값을 동시에 꺼냄
# rjust(n, '0') -> 문자열의 길이가 n이 될 때까지 왼쪽에 0을 채움
def solution1(n, arr1, arr2):
    answer = []

    # arr1과 arr2에서 같은 위치의 숫자를 하나씩 꺼냄
    # 예: i = 9, j = 30
    for i, j in zip(arr1, arr2):

        # i와 j를 비트 OR 연산
        # 결과를 이진수 문자열로 바꾸고 앞의 '0b' 제거
        # 예: 9 | 30 = 31
        # bin(31) = '0b11111'
        # [2:] = '11111'
        a12 = bin(i | j)[2:]

        # 문자열 길이가 n보다 짧으면 왼쪽에 '0'을 채움
        # 예: n이 5이고 a12가 '101'이면 '00101'
        a12 = a12.rjust(n, '0')

        # 이진수의 1을 벽을 의미하는 '#'으로 변경
        a12 = a12.replace('1', '#')

        # 이진수의 0을 공백을 의미하는 ' '으로 변경
        a12 = a12.replace('0', ' ')

        # 완성된 지도 한 줄을 정답 배열에 추가
        answer.append(a12)

    return answer
