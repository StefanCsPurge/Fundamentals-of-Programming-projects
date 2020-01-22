"""
========================
Calculating permutations
========================
"""

def init(v):
    v.append(0)

def successor(k,v,n):
    if v[k] < n:
        v[k] += 1
        return 1
    return 0

def valid(k,v):
    for i in range(1,k):
        if v[i] == v[k]:
            return 0
    return 1

def solution(k,n):
    return k == n

def printSol(m,v,n):
    strFmt = ''
    for i in range(1,n+1):
        strFmt += str(v[i])
    print("{}: {}".format(m, strFmt))
    m += 1
    return m

def Back(n):
    v = [0]
    k = 1
    m = 1
    init(v)
    while k > 0:
        isV = 0
        if k <= n:
            isS = successor(k,v,n) # daca avem successor pe poz k
            if isS: isV = valid(k,v) # daca noul successor e valid cu elem de pe poz k
            while isS and not isV:
                isS = successor(k,v,n)
                if isS: isV = valid(k,v)
            if isS:
                if solution(k,n): # daca e solutie
                    m = printSol(m,v,n)
                else:
                    k += 1
                    init(v)
            else:
                k -= 1
                v.pop()


if __name__ == '__main__':
    n = int(input("Enter n: "))
    Back(n)
