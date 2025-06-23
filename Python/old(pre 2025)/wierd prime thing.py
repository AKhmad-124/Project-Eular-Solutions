x=int(input("n-st prime number:"))
def ftest(n):
    a=3
    c=4
    while c!=n:
        c1=0
        a+=2
        for i in range(1,int(a/2)+1,1):
            if a%3==0 or a%5==0 or a%7==0 :
                break
            if a%i==0:
                c1+=1 
            if c1>1:
                break
        if c1==1:
            c+=1
    return(a)
print(ftest(x))
