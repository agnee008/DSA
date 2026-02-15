def majorityElement(nums):
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n,0)
    for n in count:
        if count[n] > len(nums)//2:
            return n