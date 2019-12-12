
'''Generate the largest perfect number smaller than a given natural number n.
If such a number does not exist, a message should be displayed.
A number is perfect if it is equal to the sum of its divisors, except itself.
'''
def divisors_sum(x):
    from math import sqrt
    s=0
    d=0
    r=int(sqrt(x))
    for d in range(2,r+1):
        if x%d==0:
            s+=d+x//d
    if d*d==x:
        s+=d
    return s+1 #sum of the proper divisors + 1

while __name__=="__main__":
    n = int(input("Give n: "))
    ok=0
    for i in range(n-1,5,-1):
        if i == divisors_sum(i):
            ok=1
            print(i)
            break
    if not ok:
        print("Non-existent")
