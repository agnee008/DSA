def sortArray(nums):
    res = set()
    while nums:
        smallest = nums[0]
        for n in nums:
            if n < smallest:
                smallest = n
        res.add(smallest)
        nums.remove(smallest)
    return res