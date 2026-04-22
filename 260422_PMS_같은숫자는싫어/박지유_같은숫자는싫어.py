def solution(arr):
    answer = []
    tmp_list = arr
    
    # 결론부터 말하면 👉 안 터지는 이유는 “or의 단락 평가(short-circuit)” 때문
    for index, val in enumerate(tmp_list):
        if not answer or answer[-1] != val:
            answer.append(val)
          
    return answer