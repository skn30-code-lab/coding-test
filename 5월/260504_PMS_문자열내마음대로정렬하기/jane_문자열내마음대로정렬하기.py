def solution(strings, n):
    new_dict = {}

    sorted_list = sorted(strings)
    for i in sorted_list:
        new_dict[i] = i[n]
        
    sorted_data = sorted(new_dict.items(), key=lambda x: x[1])
    result = [t[0] for t in sorted_data]

    answer = result
    return answer
