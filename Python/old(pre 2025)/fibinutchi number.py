x=1
y=1
z=1
c=2
while True:
    z=x+y
    y=x
    x=z
    c+=1
    if len(str(z))==1000:
        break
print(c)
    