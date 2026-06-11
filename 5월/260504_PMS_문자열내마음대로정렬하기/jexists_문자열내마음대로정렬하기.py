def solution(strings, n):

    answer = sorted(strings, key=lambda x: (x[n], x))

    return answer


    # dict = {}
    # sort_list = []
    # for str in strings:
    #     dict[str[n:]] = str
    #     sort_list.append(str[n:])
    # answer = []
    # sort_list.sort(reverse=False)
    # for s, i in enumerate(sort_list):
    #     answer.append(dict[i])
    # return answer
