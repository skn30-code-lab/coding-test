def solution(s, n):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    answer = ''
    for v in s:
        if (v == ' '):
            answer = answer + ' '
        else:
            i = alphabet.index(v.lower()) + n
            if i > (len(alphabet) - 1):
                i = i - (len(alphabet))
            if (v.isupper()):
                answer = answer + alphabet[i].upper()
            else:
                answer = answer + alphabet[i]

    return answer
