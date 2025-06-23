import time
number = 1
start_time = time.time()

def is_all_odd_and_no_zero(number):
    if number % 10 == 0:
        return False
    number_reversed = int(str(number)[::-1])
    to_check = number_reversed + number
    for i in str(to_check):
        if int(i) % 2 == 0:
            return False
    return True


counter = 0
while number <= 100000000:
    if is_all_odd_and_no_zero(number):
        counter += 1
    number += 1
end_time = time.time()
print(counter,end_time-start_time)

