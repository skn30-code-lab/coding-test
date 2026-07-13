# https://school.programmers.co.kr/learn/courses/30/lessons/120869


def solution(spell, dic):
    for d in dic:
        if all(word in d for word in spell):
            return 1
    return 2


if __name__ == "__main__":
    test_cases = [
        (["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"], 2),
        (["z", "d", "x"], ["def", "dww", "dzx", "loveaw"], 1),
        (["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"], 2),
    ]

    for i, (spell, dic, expected) in enumerate(test_cases, 1):
        result = solution(spell, dic)
        status = "O" if result == expected else "X"
        print(f"[{status}] test {i}: got={result}, expected={expected}")
