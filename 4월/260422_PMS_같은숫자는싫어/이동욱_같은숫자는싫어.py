def sol(arr):

    z=[]
    t=0

    
    while t < len(arr):
        # z가 비어있거나, 마지막 요소와 현재 요소(arr[t])가 다를 때만 추가
        if not z or z[-1] != arr[t]:
            z.append(arr[t])
    
        
        t += 1
    return z


# 아래는 for문 쓰려다 실패한 것

#     x=[]

# for index,a in enumerate(arr):
#     if x[-1] == index:
#         pass
#     else:
#         x.append(a)

# print(x)
