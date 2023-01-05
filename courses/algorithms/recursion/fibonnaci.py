
def addseq(n,b1,b2):
    if n==0:
        return b1
    else:
        return addseq(n-1,b2,b1+b2)


print(addseq(n=3,b1 = 0,b2 = 1))