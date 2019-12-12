'''
Determine  the  twin  prime  numbers p1 and p2 immediately  larger
than  the  given  non-null natural number n.
Two prime numbers p and q are called twin if q-p = 2. '''

def prime (x):
    from math import sqrt
    if x<2 or x>2 and x%2==0:
        return 0
    for d in range(3,int(sqrt(x))+1,2):
        if x%d==0:
            return 0
    return 1

while __name__=="__main__":
    n = int(input("Give n: "))
    if n % 2:
        p=n+2
    else:
        p=n+1
    ok=0
    q=0
    while not ok:
        if prime(p) and prime(p+2):
            q=p+2
            ok=1
        else: p+=2
    print(p,q,"are the twin prime numbers immediately larger than the given non-null natural number", n)
    
    
