import math
number = 3
count_of_prime = 1
number_to_div = 3
sum = 2


while number <= 2000000: 

    number_to_div =3
    is_prime = True

    while number_to_div <= (math.sqrt(number))+1:
        if number % number_to_div == 0:
            is_prime = False
            break
        number_to_div += 2 
    if is_prime :
        count_of_prime += 1
        sum += number
        print(number,count_of_prime,sum)
    number += 2
