def solution(board, moves):
    result = []
    pop = 0
    for move in moves:
        for i in range(len(board)):
            doll = board[i][move-1]
            if doll:
                if result and result[-1] == doll:
                    result.pop()
                    pop += 2
                else:
                    result.append(doll)
                board[i][move-1] = 0
                break;
    return pop

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves)) # 4