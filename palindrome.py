def isPalindrome(n : int) -> bool:
    a = 0
    m = n
    while n  > 0:
        a = a * 10 + (m%10)
        m = m // 10
    if a == n:
        return True
    else:
        return False
        
    