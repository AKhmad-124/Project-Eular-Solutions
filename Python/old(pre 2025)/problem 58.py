import pickle
import math
import time

prime_chk = pickle.loads(open("primes.pkl","rb").read())

def amount_of_devisors_by_sqrt(number):
    checker = 2
    factors = 2
    while checker <= math.sqrt(number) :
        if number % checker == 0:
            factors += 1
        checker += 1
    return ((factors-1)*2)


def get_diagonal_percentage_of_side_length(side_length):# side length must be odd
    list_of_corners = [1]
    current_number = 1
    multiplier = 2
    primes = 0
    while current_number != side_length**2:
        for i in range(1,5):
            number = current_number + i*multiplier  
            list_of_corners.append(number)
            if amount_of_devisors_by_sqrt(number) == 2:
                primes += 1

        print((current_number**(1/2))+2,primes/len(list_of_corners))
        current_number = number
        multiplier = multiplier+2

    return list_of_corners


# def get_prime_percent(list):
    
#     n = 0
#     for i in list:
#         if i in prime_chk:
#             n = n+1
#     return n/len(list)
get_diagonal_percentage_of_side_length(26593)
# side_length = 3
# while side_length <= 1001:
#     if get_prime_percent(get_corner_of_side_length(side_length)) <= 10:

#         print(side_length,get_prime_percent(get_corner_of_side_length(side_length)))
#     side_length += 2 
print(amount_of_devisors_by_sqrt(5003231))

# print(get_prime_percent(get_corner_of_side_length(7)))