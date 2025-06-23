n=int(input("enter factorial:"))
p=1
while n!=0:
    p=p*n
    n-=1
l=[int(x) for x in str(p)]
s=0
for i in range(0,len(l),1):
    s+=l[i]
print(p,s)
