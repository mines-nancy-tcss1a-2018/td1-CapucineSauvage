def puissance (a,n):
    if n==0:
        return 1
    else:
        res=1
        for k in range (1,n+1):
            res=res*a
        return res

assert (puissance (2,15)==32768)

print (puissance(2,15))

def solve(a,n):
    res= puissance (a,n)
    chiffre=str(res)
    somme=0
    for k in range (0, len(chiffre)):
        somme=somme+int(chiffre[k])
    return somme

assert(solve(2,15)==26)
print (solve(2,1000))