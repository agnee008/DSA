def power(x:int, n:int):
    res = 1
    for i in range(n):
        res *= x
    return res