#이진 스트링으로 변경
def pre_prossing(in_str):
#앞부분 '0b' 제거
    if in_str.startswith('0b'):
        tmp_str = in_str[2:]
    else:
        tmp_str = in_str
#length 맞추기
    str_len = len(tmp_str)
    print(str_len)
    cnt = 0
    occupied = 0
#포화이진트리 작성용 2의 n제곱 구하기
    while occupied < str_len:
        cnt += 1
        occupied = 2 ** cnt - 1
#포화이진트리 작성
    result = '{}{}'.format('0' * (occupied - str_len), tmp_str)
    return result
#미드 인덱스 찾기
def mid_index(in_str):
    str_len = len(in_str)
    mid_idx = str_len // 2
    return mid_idx
#이진 트리에서 부모 노드, 자식 노드 뽑기
def node_check(in_str):
#엣지케이스 처리를 위한 코드: numbers 의 길이가 1 이면 left, right가 '' 으로 나옴
        if len(in_str) <= 1:
            return True
#노드 체크 핵심은 부모 노드가 0일때 자식 노드도 전부 0인지 여부를 확인해야 함
    if len(in_str) == 3:
        mid = in_str[1]
        left, right = in_str[0], in_str[2]
        if mid == '0':
            if in_str == '000':
                return True
            else:
                return False
        else:
            return True
    else:
        mid = mid_index(in_str)
        mid_num = in_str[mid]
        left, right =  in_str[:mid], in_str[mid+1:]
        left_mid, right_mid = left[mid_index(left)], right[mid_index(right)]
        if in_str[mid] == '0':
            if all(c == '0' for c in in_str):
                return True
            else:
                 return False
        else:
            return left, right
#노드 체크 반환값이 3개이므로 이걸 기준으로 솔루션을 짜야 한다.
def check(in_str):
    result = node_check(in_str)
    if result == False:
        return 0
    if result == True:
        return 1
    #여기까지 온 경우라면, left, right가 반환됨(재귀 사용)
    left, right = result
    return min(check(left), check(right)) # 둘 중 작은 값으로 반환 ; 양쪽 다 안되면 불가능

def solution(numbers):
    answer = []
    for num in numbers:
        in_bin_str = pre_prossing(bin(num))
        answer.append(check(in_bin_str))
    return answer
print(solution([7, 42, 5]))
print(solution([63, 111, 95]))
