# 문제
# 시저암호: 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식
# ex) "AB"는 1만큼 밀면 "BC", 3만큼 밀면 "DE", "z"는 1만큼 밀면 "a"
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수 생성하기

# 제한 조건
# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.


def solution(s, n):
    answer = ''

    # 문자열 s에서 글자를 하나씩 꺼내와서 확인
    for letter in s:
        # 1. 공백의 경우: 공백은 몇 번을 밀어도 공백이므로 그대로 더하기
        if letter == ' ':
            answer += ' '

        # 2. 대문자의 경우
        elif letter.isupper():
            # A를 기준으로 얼마나 밀어야 하는지 번호(코드)를 계산
            new_num = (ord(letter) - ord('A') + n) % 26 + ord('A')
            # 계산된 번호를 다시 글자로 바꿔 정답에 붙임
            answer += chr(new_num)
            
        # 3. 소문자의 경우
        elif letter.islower():
            # 대문자와 동일하지만 기준만 소문자 'a'로
            new_num = (ord(letter) - ord('a') + n) % 26 + ord('a')
            answer += chr(new_num)
            
    return answer