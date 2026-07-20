def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        binary_num = format(arr1[i] | arr2[i], f'0{n}b')
        result = binary_num.replace('1', '#').replace('0', ' ')
        answer.append(result)

    return answer