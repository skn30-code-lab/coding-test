def solution(board, moves):
    # 각 열(Column)에서 0을 제외한 인형만 추출한 뒤, pop()하기 쉽게 역순 정렬
    cols = [list(filter(None, col))[::-1] for col in zip(*board)]
    stack = []
    result = 0

    for m in moves:
        col = cols[m - 1]
        if col:
            doll = col.pop()
            if stack and stack[-1] == doll:
                stack.pop()
                result += 2
            else:
                stack.append(doll)
                
    return result
