#cmmdc

def gcdiv (x,y):
    while y:
        r=x%y
        x=y
        y=r
    return x

def gcd (x,y):
    if not y: return x
    return gcd(y,x%y)


print(gcdiv(90,24),gcd(90,24))
