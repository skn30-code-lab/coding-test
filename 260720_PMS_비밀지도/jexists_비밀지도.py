def solution(n, arr1, arr2):
    first = []
    second = []
    len = n

    for x in arr1:
      # print(bin(x))
      # print(f"{x:0{len}b}")
      first.append(list(f"{x:0{len}b}"))

    for y in arr2:
      second.append(list(f"{y:0{len}b}"))
    answer = []
    for i in range(n):
      text = ''
      for j in range(n):
        if first[i][j] == '1' or second[i][j] == '1':
            text = text + '#'
        else:
            text = text + ' '
      answer.append(text)
    return answer
