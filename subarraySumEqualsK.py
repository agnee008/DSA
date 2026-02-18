def subsumequalsK(nums, k):
    curSum = 0
    prefixSum ={0:1}
    res = 0
    
    for n in nums:
        curSum += n
        diff = curSum - k
        res += curSum.get(diff, 0)
        prefixSum[curSum] = 1 + prefixSum.get(curSum,0)
    return res