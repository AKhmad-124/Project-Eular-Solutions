file_of_names = open("0022_names.txt","r")#opens the folder (file name.extension , read-only or smthn else )

text_of_names = file_of_names.read()#puts all the text into a single string

names_no_quots = text_of_names.replace('"',"")#removes all ""

list_of_names = names_no_quots.split(",")#makes string into a list with , as the split point

list_of_names.sort()#sorts the names in-place
list_of_letter_sums = []


for name in list_of_names:
    sum = 0
    list_of_letters = list(name)
    for letter in list_of_letters:
        if letter == "A":
            sum = sum + 1
        elif letter == "B":
            sum = sum + 2
        elif letter == "C":
            sum = sum + 3
        elif letter == "D":
            sum = sum + 4            
        elif letter == "E":
            sum = sum + 5
        elif letter == "F":
            sum = sum + 6
        elif letter == "G":
            sum = sum + 7
        elif letter == "H":
            sum = sum + 8
        elif letter == "I":
            sum = sum + 9
        elif letter == "J":
            sum = sum + 10
        elif letter == "K":
            sum = sum + 11
        elif letter == "L":
            sum = sum + 12
        elif letter == "M":
            sum = sum + 13
        elif letter == "N":
            sum = sum + 14
        elif letter == "O":
            sum = sum + 15
        elif letter == "P":
            sum = sum + 16
        elif letter == "Q":
            sum = sum + 17
        elif letter == "R":
            sum = sum + 18
        elif letter == "S":
            sum = sum + 19
        elif letter == "T":
            sum = sum + 20
        elif letter == "U":
            sum = sum + 21
        elif letter == "V":
            sum = sum + 22
        elif letter == "W":
            sum = sum + 23
        elif letter == "X":
            sum = sum + 24
        elif letter == "Y":
            sum = sum + 25
        elif letter == "Z":
            sum = sum + 26
        # print(letter,sum)
    list_of_letter_sums.append(sum)
print(list_of_letter_sums)

index = 1
sum_final = 0
for i in list_of_letter_sums:
    sum_final = sum_final + (i * index)
    index = index + 1
    print(i*index)


print(sum_final)












file_of_names.close()