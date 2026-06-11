count = 0
def dfs(index,total,num_list,target):       # index 기준으로 순회하며 count 증가시키는 함수
    global count
    
    if index == len(num_list):          # index 끝 도달
        if total == target:             # 길이가 맞고 값도 맞을 경우에만 count 증가
            count += 1
        return
    
    dfs(index+1,total + num_list[index],num_list,target)    # 양수의 경우  
    dfs(index+1,total - num_list[index],num_list,target)    # 음수의 경우


def solution(num_list,target):
    dfs(0,0,num_list,target)    # 0,0 시작
    
    return count

# num_list = [1,1,1,1,1]
# target = 3


    
    
    