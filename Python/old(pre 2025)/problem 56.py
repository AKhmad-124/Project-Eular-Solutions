a = 1
b = 1
max = 0

def sum_of_digits_in_number(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum

while a<= 100:
    b = 1 
    while b <=100:
        number = sum_of_digits_in_number(a**b)
        if max < number:
            max = number
            print(max,a**b)
        b += 1
    a += 1



