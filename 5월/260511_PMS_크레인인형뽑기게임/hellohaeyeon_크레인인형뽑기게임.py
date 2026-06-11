def solution(board, moves):
    stack = []
    crain = 0
    pang = 0
    b_xlen = len(board[0]) #리스트 하나의 길이
    b_ylen = len(board)    #리스트 묶음의 길이
    converted_dic = {}
    #list convert
    for i in range(b_xlen):
        tmp_list = []
        for j in range(b_ylen):
            if board[j][i] != 0: #0이 아닌 모든 요소 담기
                tmp_list.append(board[j][i])
        converted_dic[i + 1] = tmp_list[::-1] #역순으로 변경(stack화)
    for num in moves:
        crain = 0 # crain 초기화
        try:
            crain = converted_dic[num].pop() #dic에서 집어오기
        except:
            continue
        if crain:
            if not stack: #case1: 비어있는 경우
                stack.append(crain)
            elif stack and stack[-1] == crain: #case2: stack의 마지막 요소와 crain 이 같은 경우(펑)
                stack.pop()
                pang += 2
            else: #case3: 다른 경우 - stack에 추가
                stack.append(crain)
    return pang
test_board =[[0,0,0,0,0],
             [0,0,1,0,3],
             [0,2,5,0,1],
             [4,2,4,4,2],
             [3,5,1,3,1]]
test_move = [1,5,3,5,1,2,1,4]
print('board: {}\nmove: {}\nanswer: {}'.format(test_board, test_move, solution(test_board, test_move)))
