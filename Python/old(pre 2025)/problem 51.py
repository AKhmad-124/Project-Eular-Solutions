import math
def list_of_number_recureance(number_to_analyze):
    list_of_recureance = [0,0,0,0,0,0,0,0,0,0]
    for i in str(number_to_analyze):
        if int(i) == 0 :
            list_of_recureance[0] +=1
        if int(i) == 1 :
            list_of_recureance[1] +=1
        if int(i) == 2 :
            list_of_recureance[2] +=1
        if int(i) == 3 :
            list_of_recureance[3] +=1
        if int(i) == 4 :
            list_of_recureance[4] +=1
        if int(i) == 5 :
            list_of_recureance[5] +=1
        if int(i) == 6 :
            list_of_recureance[6] +=1
        if int(i) == 7 :
            list_of_recureance[7] +=1
        if int(i) == 8 :
            list_of_recureance[8] +=1
        if int(i) == 9 :
            list_of_recureance[9] +=1
    return(list_of_recureance)


def is_prime(number):#feed only odd numbers
    checker = 3
    while checker <= math.sqrt(number):
        if number % checker == 0:
            return False
        checker +=2
    return True
# number = 3
# while number

primes_2 = []
primes_3 = []
primes_4 = []
primes_5 = []
primes_6 = []
number = 11
while number != 999999:
    if is_prime(number):
        if len(str(number)) == 2:
            primes_2.append(int(number))
        if len(str(number)) == 3:
            primes_3.append(int(number))
        if len(str(number)) == 4:
            primes_4.append(int(number))
        if len(str(number)) == 5:
            primes_5.append(int(number))
        if len(str(number)) == 6:
            primes_6.append(int(number))
    number += 2






