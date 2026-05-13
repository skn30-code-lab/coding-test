def solution(s):
    num = ['zero', 'one','two', 'three', 'four', 'five', 'six','seven', 'eight','nine']

    for i, n in enumerate(num):
        s = s.replace(n, str(i))

    answer = int(s)

    return answer

