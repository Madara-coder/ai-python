# List methods

numbers = [ 5,2,1,7,4,1,1]

numbers.append(20)# adds 20 in last of the lists
print(numbers)
numbers.insert(2,32)# inserts 32 in 2 location
print(numbers)
numbers.remove(5)# removes the digit 5
print(numbers)
#numbers.clear()#removes all the element
# numbers.pop()
print(numbers.count(1))# counts the numbers of 1 in numbers variable

numbers.sort()# sorts the numbers in asccending order
print(numbers)

numbers.reverse()# reverses the elements present in the lists
print(numbers)


# =============================================================================
# 
# =============================================================================
numbers2 = numbers.copy()# copies from the numbers list to numbers2
numbers2.append(23)
print(f"This is the second list:- {numbers2}")