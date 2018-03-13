def findFirstIndex(L,x):
    i=0
    while i<len(L):
        if L[i]==x:
            return i
        else:
            i=i+1
    return -1

def findAllIndices(L,x):
    i=0
    a=[]
    while i < len(L):
        if L[i]== x:
            c=i
            a[len(L):len(L)]=[c]
            i=i+1
        else:
            i=i+1
    return a

def removeLastCopy(L,a):
    p=findAllIndices(L,a)
    if p==[]:
        return L[:]
    else:
        o=L[:]
        s=p[len(p)-1]
        o[s:s+1] = []
        return o
