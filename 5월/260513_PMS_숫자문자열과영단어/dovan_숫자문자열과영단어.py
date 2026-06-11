def solution(s):
    # 영단어와 숫자의 매핑 딕셔너리 정의
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    # 딕셔너리를 순회하며 문자열 내의 영단어를 대응되는 숫자로 치환
    for word, digit in num_dict.items():
        s = s.replace(word, digit)
        
    return int(s)

# def solution(s):
#     dict = {'zero' : 0,
#            'one' : 1,
#            'two' : 2,
#            'three' : 3,
#            'four' : 4,
#            'five' : 5,
#            'six' : 6,
#            'seven' : 7,
#            'eight' : 8,
#            'nine' : 9}
#     result = []
#     result1 = []
#     for i in list(s):
#         result.append(i)
#         if result in list(dict.keys()):
#             result1.append(result)
#         else:
#             result1.append(result)
#     return result1
