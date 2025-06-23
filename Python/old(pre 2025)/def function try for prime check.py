def ftest(p):
    u=False
    c2=0
    for g in range(1,int(p/2)+1,1):
        if p%g==0:
            c2+=1 
            
        if c2>1 or p==1 :
            u=False
            break
        if c2==1:
            u=True

            #put action here
    return(u)
print(ftest(739397))
#put action here
n = 1
while n<= 500 :
    if ftest(n):
        print(n)
    n+=1