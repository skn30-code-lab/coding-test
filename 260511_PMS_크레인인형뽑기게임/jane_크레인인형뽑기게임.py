def solution(board, moves):
    basket = []
    tmp = []
    answer = 0

    # moves 순서대로 크레인 이동
    for move in moves:
        col = move
        
        # 위에서 아래로 탐색
        for row in board:
            if row[col-1] == 0:
                pass
            else:
                if basket:

                    # 바구니 맨 위 인형
                    tmp = basket[-1]

                    # 현재 뽑은 인형과 바구니 맨 위 인형 비교
                    if row[col-1] == tmp:
                        answer += 2
                        basket.pop()
                    else:
                        basket.append(row[col-1])
                else:
                    basket.append(row[col-1])
                row[col-1] = 0
                break
   
    return answer