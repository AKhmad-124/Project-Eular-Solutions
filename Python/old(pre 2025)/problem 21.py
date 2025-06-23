import math


def sum_of_factors(number):
    checker = 2
    sum = 1
    while checker <= number/2:
        if number % checker == 0:
            sum += checker
        checker += 1
    return sum

sum = 0

number = 2
while number <= 10000:
    if number == sum_of_factors(sum_of_factors(number)) != sum_of_factors(number):
        print(number,sum_of_factors(number))
        sum += number
    number += 1
print(sum)