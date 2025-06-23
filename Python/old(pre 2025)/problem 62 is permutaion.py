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
number_and_list_pair = {}
number  = 1
repeats = 4
while number <= 10000:
    current_repeat = 0
    current_list = list_of_number_recureance(number ** 3)
    for i in number_and_list_pair:

        if current_list == number_and_list_pair[i]:
            current_repeat += 1
    if current_repeat == repeats:
        for i in number_and_list_pair:
            if current_list == number_and_list_pair[i]:
                print(number,i,current_list)
        print(number,current_list)
    

    number_and_list_pair[number] = current_list
    number +=1
# print(number_and_list_pair)
