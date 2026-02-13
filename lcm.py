def lcm(a : int,b : int) -> int:
    res = []
    for i in range(1, b+1):
        if (a * i) % b == 0:
            res.append(a*i)
    return min(res)