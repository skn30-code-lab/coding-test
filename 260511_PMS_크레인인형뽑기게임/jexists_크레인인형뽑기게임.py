def solution(board, moves):
    cart = []
    answer = 0

    for m in moves:
        for b in board:
            if b[m - 1] != 0: # 아무것도 없는 경우가 아나라면
                prev = None
                if cart != []: # 바구니에 죠르디가 있다면
                    prev = cart[-1] # 이전거 체크 (현재거랑 비교하기 위해)
                if prev != None and prev == b[m - 1]: # 이전거랑 현재거 비교해서 같은경우
                    answer += 2 # 터진 인형의 개수 더하기
                    cart.pop() # 같은거 없애기
                else: # 이전거랑 현재거랑 다르면 죠르디 넣기
                    cart.append(b[m - 1])
                b[m - 1] = 0 # 옮긴 죠르디 없애기
                break

    return answer

# b = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# m = [1,5,3,5,1,2,1,4]
# 답: 4
# solution(b, m)

# [4, 3, 1, 1, 3, 2, 4]

# [0,0,0,0,0]
# [0,0,1,0,3]
# [0,2,5,0,1]
# [4,2,4,4,2]
# [3,5,1,3,1]
