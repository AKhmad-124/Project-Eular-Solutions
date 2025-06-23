number = 1
list = []
while number <= 1000000:
    for i in str(number):
        list.append(int(i))
    number += 1
print(list[0]*list[9]*list[99]*list[999]*list[9999]*list[99999]*list[999999])