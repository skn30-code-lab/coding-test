def solution(lines):
	counter = {}
	for start, end in lines:
			for i in range(start, end):
				counter[i] = counter.get(i, 0) + 1
    
	answer = 0
	for value in counter.values():
		if value >= 2:
			answer += 1
    
	return answer


lines = [[[0, 1], [2, 5], [3, 9]],		# 2
		 [[-1, 1], [1, 3], [3, 9]],		# 0
		 [[0, 5], [3, 9], [1, 10]]]		# 8

for line in lines:
    print(f"{line}:\n{solution(line)}\n")