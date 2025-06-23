def factorial(number):
    product = 1
    while number >= 2:
        product *= number
        number  -= 1
    return product


number = 10
for i in range(10,1000000,1):
    list_of_numbers = list(str(number))
    
    sum = 0
    list_factorialed = []
    for i in list_of_numbers:
        list_factorialed.append(factorial(int(i)))
    for i in list_factorialed:
        sum += i
    if sum == number :
        print(number,list_factorialed,sum)

    number += 1
