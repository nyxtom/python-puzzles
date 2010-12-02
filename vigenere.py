import string

def vigenere(c,k,e=1):
# e=1 to encrypt, e=-1 to decrypt
    wk=[string.ascii_uppercase.find(ch) for ch in k.upper()]
    wc=[string.ascii_uppercase.find(ch) for ch in c.upper()]


    wc = [ (x[0]+(e*x[1]))%26 for x in zip(wc,wk*(len(wc)/len(wk)+1))]

    print string.join([string.ascii_uppercase[x] for x in wc],"")
