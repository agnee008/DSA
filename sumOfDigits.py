def sumOfDigits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def sumOfDigitsRecursion(n):
    if n < 10:
        return n
    return n%10 + sumOfDigitsRecursion(n//10)