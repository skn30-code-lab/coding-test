def solution(nums):
# 최대로 가질수 있는 폰켓몬 종류의 수: half_nums
# 다만 uniq_nums가 그보다 작은 경우 uniq_nums 를 따라가게 됨
    half_nums = len(nums) // 2
    uniq_nums = len(set(nums))
    # answer = 0
    if uniq_nums <= half_nums:
        return uniq_nums
    return half_nums