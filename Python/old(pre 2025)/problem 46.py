import math
import sys
def is_prime(number):#feed only odd numbers
    checker = 3
    while checker <= math.sqrt(number):
        if number % checker == 0:
            return False
        checker +=2
    return True



number = 3
while number < 1000000:
    if  not is_prime(number):
        d = 1
        x = number-(2*(d**2))
        flag = False
        while x >= 0:
            if is_prime(x):
                flag = True
                break
            d += 1
            x = number-(2*(d**2))
        if not flag:
            print(number)
    number += 1



