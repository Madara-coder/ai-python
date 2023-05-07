"""
 DATA STRUCTURE;
There are thre types of the data structure in python. Namely:-
1. List- It is ordered data structure that can store multiple data along with 
        repetition.Eg: a = [1,2,3,4,5]
                        b= [] //empty list
                        c= ['ram','binod','debrath']
        It is mutable data-type, that means it can be altered.
       -> c.append('gita') - adds gita element at last in c variable
       -> c.insert(2, "Beeshow") - inserts the element in the 2 location of the list
       -> c[2] = "Beeshow" - alternate to above 
       
    Accessing items from the list:-
     a[3]   - output will be 4 
     
     a.pop() - returns the last element.
     a.pop(2) - returns the elemnt presnt in the location 2.
     a.reverse() - helps to reverse the element of the list a 
    
    
2. Tuple
3. Dictionary.


"""

#CLASSWORK
a = [1,10,20,40,50]
b = []
i= 4
while i>=0: 
    #print(i)
    b = a[i]
    print(b)
    i = i- 1
    
    
    
c = ['Ram','Sita','Gita',"Hari"]
d = []
j = 3
while j>=0:
    d = c[j]
    print(d)
    j -= 1
 

       
        
    
    

