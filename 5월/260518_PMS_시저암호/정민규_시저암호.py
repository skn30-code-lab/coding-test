def solution(s, n):
    small = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    answer = ""
    
    for i in s:
        if i in small:
            k = small.find(i)
            answer += small[k + n]
        elif i in big:
            k = big.find(i)
            answer += big[k + n]
        elif i == " ":
            answer += " "
            
    return answer