def solution(lines):
	answer = 0
	return answer


lines = [[[0, 1], [2, 5], [3, 9]],		# 2
		 [[-1, 1], [1, 3], [3, 9]],		# 0
		 [[0, 5], [3, 9], [1, 10]]]		# 8

for line in lines:
	print(f'{line}:{'\n'}{solution(line)}{'\n'}')