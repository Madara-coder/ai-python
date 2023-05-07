# Finding the maximum numbers in the lists

numbers = [3,6,2,8,3,4,5,2,11,34]

max = numbers[0]

for number in numbers: #By default number is the variable having the first positive number
    if number > max:
        max = number
print(max)