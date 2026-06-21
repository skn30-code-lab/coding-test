def solution(ingredient):
    answer = 0
    basket = []

    for i in ingredient:
        basket.append(i)

        if len(basket) >= 4 and basket[-4:] == [1, 2, 3, 1]:
            answer += 1
            del basket[-4:]

    return answer

# ==============================

# def solution(ingredient):
#     answer = 0
#     basket = []
    
#     for item in ingredient:
#         basket.append(item)
        
 
#         if basket[-4] == 1 and basket[-3] == 2 and basket[-2] == 3 and basket[-1] == 1:
#             answer += 1
#             basket.pop()
#             basket.pop()
#             basket.pop()
#             basket.pop()
                
#     return answer