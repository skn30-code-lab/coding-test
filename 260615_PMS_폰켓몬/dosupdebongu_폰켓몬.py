def solution(nums):
    
    nums.sort()
    answer = 0

    if len(nums)>0:
        count = 1
    else:
        count = 0

    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            count+=1

    max_length = len(nums)//2
    
    if count < max_length:
        answer = count
    else:
        answer = max_length
    return answer