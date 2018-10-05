f=open('p022_names.txt','r')
for ligne in f:
    chaine=ligne
f.close

def ordre_alphabetique(x):
    return sorted(x, key=str.lower)


def worth(n):
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    valeur=0
    for e in n:  
        for j in range (0,26):
            if e==alphabet[j]:
                valeur+=j+1
    return valeur

assert (worth('COLIN')==53)

def solve():
    x=chaine.split(",")
    liste=ordre_alphabetique(x)
    total=0
    for k in range (0, len(liste)):
        n=liste[k]
        score=worth(n)*(k+1)
        total+=score
    return total

print(solve())