import sys
import math
icing  = True
angle = 0
a = 9
b = 10
c = 11

x = 360 / a
y = 360 / b
z = 360 / c
list = [x,y,z]
counter = 0 
while 1:
    for i in list:
        angle += i
        counter += 1
        if angle >=360:
            angle -= 360
            icing = not icing
        if icing and angle == 0:
            print(counter,angle,icing)
            sys.exit()
        # print(counter,angle,icing,list)
    

    
