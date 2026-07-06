def solution(ham):
    a=[]
    for i in ham :
        a.append(i)
        if a[-4:] == [1,2,3,1]:
            a.pop()
            a.pop()
            a.pop()
            a.pop()
    return (len(ham)-len(a))//4