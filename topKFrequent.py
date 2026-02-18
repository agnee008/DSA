def topKFrequent(nums, k):
    freq = [[] for i in range(len(nums) + 1)]
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n,0)
        
    for n,c in count.items():
        freq[c].append(n)
    res = []
    
    for i in range(len(nums) -1, 0, -1):
        for n in freq[i]:
            if len(res) == k:
                return res
    return []