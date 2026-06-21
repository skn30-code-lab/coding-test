def solution1(ingredient):
    stack = []
    answer = 0

    for x in ingredient:
        stack.append(x)

        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            del stack[-4:]

    return answer

# 문자열 replace 방식은 왜 시간초과가 날까요?
# replace()가 호출될 때마다 새로운 문자열을 생성하고, while문에서 전체 문자열을 계속 탐색하므로 O(N²)에 가까워집니다. 
# 스택을 사용하면 뒤의 4개만 확인하므로 O(N)에 해결할 수 있습니다.
def solution(ingredient):
    answer = 0
    
    tmp_str = ''.join(map(str, ingredient))
    
    while "1231" in tmp_str:
        answer += 1
        tmp_str = tmp_str.replace("1231", "", 1) 
    
    return answer
