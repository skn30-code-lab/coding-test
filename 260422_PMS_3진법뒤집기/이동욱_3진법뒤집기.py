

def solution(n):
    x = []
    
    while n > 0:
        x.append(n % 3)
        n //= 3


    answer = 0
    
    for index, i in enumerate(reversed(x)):
        answer += (3*index) i

    return answer




# 내가 짠 90점 코드
# def sol(n):
#     x=[]
#     bb=[]
#     while (n//3)>0:

#         b=n%3
#         x.append(b)
#         n=n//3
#         if n//3==0:

#             x.append(n%3)




#             a=x[::-1]

#             for index,i in enumerate(a):

#                 bb.append((3*index)i)


#             return sum(bb)