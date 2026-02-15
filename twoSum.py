def twoSum(nums, k):
    available_num = {}
    for i in range(len(nums)):
        required_sum = k - nums[i]
        if required_sum in available_num:
            return (available_num[required_sum], i)
        else:
            available_num[nums[i]] = i