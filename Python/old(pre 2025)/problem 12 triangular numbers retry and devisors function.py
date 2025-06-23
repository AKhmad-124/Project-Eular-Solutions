import math


def amount_of_devisors_by_sqrt(number):
    checker = 2
    factors = 2
    while checker <= math.sqrt(number) :
        if number % checker == 0:
            factors += 1
        checker += 1
    return ((factors-1)*2)



number = 1
to_add = 2
while number <= 100000000:

    if number % 10 ==0:
        i = amount_of_devisors_by_sqrt(number)
        if i > 500:
            print(number,i)
        

    number += to_add
    to_add += 1


