n=eval(input("enter a string"))
if(type(n)==str and n[0] in 'aeiouAEIOU'):
    n=n[1::]
    print(n)
    