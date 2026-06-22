def solution(ingredient):
    hamburger = []
    answer = 0
    for i in ingredient:
        hamburger.append(i)
        if hamburger[-4:] == [1,2,3,1]:
          answer += 1
          # hamburger = hamburger[:-4]
          hamburger.pop()
          hamburger.pop()
          hamburger.pop()
          hamburger.pop()

    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))	# 2
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))	# 0
