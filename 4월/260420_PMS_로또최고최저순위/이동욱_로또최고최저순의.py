def solution(lottos, win_nums):

    list1 = [6,6,5,4,3,2,1]         # 0개, 1개까지는 낙첨, 이외에는 5등부터 시작해서 당첨
    x=[]
    for i in lottos:
        if i==0:                    
            x.append(i)
    zero=len(x)                     # 0을 따로 담아둠
    low=list1[len(set(lottos) & set (win_nums))] # 0이 모두 낙첨일 때


    high=list1[(len(set(lottos) & set (win_nums))+zero)] # 0이 모두 당첨일 때
    
    return (high,low)