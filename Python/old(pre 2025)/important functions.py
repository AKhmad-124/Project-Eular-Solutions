import math
def amount_of_devisors_by_sqrt(number):
    checker = 2
    factors = 2
    while checker <= math.sqrt(number) :
        if number % checker == 0:
            factors += 1
        checker += 1
    return ((factors-1)*2)

def is_prime(number):#feed only odd numbers
    checker = 3
    while checker <= math.sqrt(number):
        if number % checker == 0:
            return False
        checker +=2
    return True


def sum_of_digits_in_number(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum

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