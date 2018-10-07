def palindrome(n):
    a=str(n)
    b=str()
    for k in range (-1,-len(a)-1,-1):
        b=b+a[k]
    if b==a:
        return True
    else :
        return False

#print (palindrome(15951))

def reverse(n):
    a=str(n)
    r=str()
    for k in range (-1,-len(a)-1,-1):
        r=r+a[k]
    return int(r)

#print (reverse(54321))

def lychrel(n):
    c=0
    u=n
    while c<=50:
        v=u+reverse(u)
        if palindrome(v)==True:
            return False
        else:
            u=v
            c+=1
    return True
    
def solve(n):
    liste=[]
    for k in range (1,n):
        if lychrel(k)==True:
            liste=liste+[k]
    return len(liste)

print(solve(10000))


                
