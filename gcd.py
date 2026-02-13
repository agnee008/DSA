def gcd(a:int, b:int) -> int:
    res = []
    for i in range(1, min(a,b) +1):
        if a % i == b % i:
            res.append(i)
    return max(res) 

# Euclidean Method:
def gcd_optimized(a:int, b:int):
    while b!= 0:
        a ,b = b, a % b
    return a

