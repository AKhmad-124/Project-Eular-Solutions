x = 44
def sum_square_integers(x):
    y = list(str(x))
    z = 0
    for i in y:
        z = z + int(i)**2
    return z
counter = 0

for i in range(1,10000000,1):
    x = i
    while x != 1 and x!=89 :
        x = sum_square_integers(x)
    if x == 89:
        counter+=1
        print(counter,x,i)

print(counter)
