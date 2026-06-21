def solution(ingredient):
    answer = 0
    basket = []

    for i in ingredient:
        basket.append(i)

        if len(basket) >= 4 and basket[-4:] == [1, 2, 3, 1]:
            answer += 1
            del basket[-4:]

    return answer
