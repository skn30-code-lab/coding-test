def solution(s):
	answer = ''
	temp = ''
	num = ['zero','one','two','three','four','five','six','seven','eight','nine']
	while s:
		for i,n in enumerate(s):
			if n in '0123456789':
				answer += n
				s = s[i+1:]
				break;
			temp += n
			if temp in num:
				answer += str(num.index(temp))
				temp = ''
				s = s[i+1:]
				break;
	return int(answer)

s = ["one4seveneight","23four5six7","2three45sixseven","123"]
for n in s:
	print(solution(n))
#1478
#234567
#234567
#123