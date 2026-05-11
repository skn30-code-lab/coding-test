import numpy as np
def solution(board,move):    
    b=np.array(board).T     # 역행렬
    f=[]
# move = [1,5,3,5,1,2,1,4]

    for l,v in enumerate(move):
        for p,d in enumerate(b[v-1]):   # board를 예제 그림처럼 만든 후 각 열을 move 순서대로 담음

            if d != 0:                  # 빈공간이 아니면 담기
                f.append(d)
                b[v-1][p]=0             # 이후 담아진 부분은 0으로 채우기
                break
    f1 = f[::-1]                        # 추가한 인형들을 아래부터 쌓이게 만들기
    
    mm = []
    for r in f1:
        if mm and r == mm[-1]:          # 바구니가 빈상태가 아니면서 마지막 담긴게 같으면 pop
            if mm and r  == mm[-1]: 
                mm.pop(-1) 
        else:
            if not mm or r != mm[-1]:   # 바구니가 빈상태거나 같은 인형이 담긴게 아니면 추가
                mm.append(r) 
    return len(f1)-len(mm)              # 담긴 전체 인형의 수 - 현재 남은 인형의 수 = 없어진 인형의 수