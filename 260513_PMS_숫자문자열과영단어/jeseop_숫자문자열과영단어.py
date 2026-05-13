def solution(string):
	answer = ''
	temp = ''
	num = ['zero','one','two','three','four','five','six','seven','eight','nine']
	
	for char in string:
		if char in '0123456789':
			answer += char
			continue
		temp += char
		if temp in num:
			answer += str(num.index(temp))
			temp = ''
	return int(answer)

s = ["one4seveneight","23four5six7","2three45sixseven","123"]
for n in s:
	print(solution(n))
#1478
#234567
#234567
#123