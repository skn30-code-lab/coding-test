def solution(spell, dic):
    answer = 2 # defualt
    spell_set = set(spell)
    spell_len = len(spell)
    for d in dic:
        if len(d) == spell_len:
            compare_set = set(list(d))
            if compare_set == spell_set:
                answer = 1
                return answer
    return answer
