"""
IP- [10,30,30,10,30,30,20]
OP- 20

20 is only repeated odd times

"""
from typing import List
def countOdd(nums: List[int]):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n,0) + 1
    for n in freq:
        if freq[n] % 2 !=0:
            return n
    return []


# Using XOR
def countOddXor(l: List[int]):  # noqa: E741
    res = 0
    for num in l:
        res ^= num
    return res
