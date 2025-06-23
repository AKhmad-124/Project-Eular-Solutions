number = 3
count_of_prime = 1
number_to_div = 3



while number <= 1000000: 

    number_list = list(str(number))
    for i in number_list:
        if int(i) % 2 == 0:
            number += 2
            break
        

    number_to_div =3
    counter = 0

    while number_to_div <= (number**(0.5))+1:
        if number % number_to_div == 0:
            counter += 1
            break
        number_to_div += 2 
    if counter == 0:
        count_of_prime += 1
        print(number,count_of_prime)
        
    number += 2



            

    
