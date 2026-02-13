def factorial(n:int):
    res = 1
    while n > 0:
        res *= n
        n-=1
    return res