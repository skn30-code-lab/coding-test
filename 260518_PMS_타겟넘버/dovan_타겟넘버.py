def solution(numbers, target):
    # 초기 상태: 누적합 0을 만드는 방법 1가지
    dp = {0: 1}
    
    for num in numbers:
        next_dp = {}
        for total, count in dp.items():
            # 더하는 경우의 수 누적
            next_dp[total + num] = next_dp.get(total + num, 0) + count
            # 빼는 경우의 수 누적
            next_dp[total - num] = next_dp.get(total - num, 0) + count
        dp = next_dp
        
    return dp.get(target, 0)
