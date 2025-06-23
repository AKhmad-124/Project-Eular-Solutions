#1002001
# gap = 1
# gap_length = 1
# counter = 0
# for number in range(3,25,1):
#     if  gap == gap_length:
#         gap = 0
#         counter += 1
#         print(number,counter)
#     if counter == 4 :
#         counter = 0
#         gap_length +=2
#         print("gap increase",0)
#     else :
#         gap += 1
n = 3
to_add =2
counter = 1
sum = 1
limit = 1001*1001
while n<=limit:
    sum += n
    if counter == 4:
        to_add +=2
        counter = 0
    n += to_add
    counter += 1
print(sum)
    