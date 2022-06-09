
#For a given natural number n find the minimal natural number m formed with the same digits.

def construct_apparitions(n):
    a = [ 0 for i in range(10)]
    while n:
        a[n%10]+=1
        n//=10
    return a

def det_min(a):
    m = 0
    if a[0]:
        for i in range(1,10):
         if a[i]:
            m = i
            a[i]-=1
            break
    for i in range(10):
        for j in range(0,a[i]):
            m = m*10 + i
    return m


while __name__=="__main__":
    n = int(input("Give the natural number: "))
    ap = construct_apparitions(n)
    print("The smallest number is", det_min(ap))
    
    
