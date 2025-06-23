import plotly.express as ply
theta =[]
df = ply.data.wind()
r= []
n = 1
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




while n <= 10000:
    if ftest(n):
        r.append(n)
    n += 1



for i in r :



    j = i * 180/3.14
    print(i,j)
    theta.append(j)

fig = ply.scatter_polar(df,r,theta)
fig.show()