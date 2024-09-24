n=eval(input ("enter the special char :"))
d={}
if len(n)==1 and not('a'<=n<='z' or 'A'<=n<='Z' or '0'<=n<='1') and (ord(n))%5==0:
    d[n]=ord(n)
    print(d)