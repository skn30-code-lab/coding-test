def solution(arr, l, r):
    answer = []
    brr =[]
    for i in arr:
        for j in range(i):
            brr.append(i)
    K=0
    for z in range(l-1,r):
        K +=brr[z]
    C=0
    for a in brr:
        if len(answer)==r-l+1 and sum(answer)==K:
            C+=1
    return [K,C]

# C를 어떻게 구해야할까요