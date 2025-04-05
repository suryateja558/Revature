#Tuple

fruits = ("apple", "banana", "cherry")
print(fruits)  


single_element = ("apple",)
print(type(single_element))  


num = 1, 2, 3
print(num) 


fruits = ("ram", "raghu", "raju")
print(fruits[0])  
print(fruits[-1])  
print(fruits[1:3])  


fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)


fruits = ("apple", "banana", "cherry")
print(len(fruits)) 


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)


new_tuple = tuple1 + tuple2
print(new_tuple) 


num = (10, 20, 30, 40)
print(num.index(30)) 


num= (1, 2, 3, 2, 2, 4, 5)
print(num.count(2)) 


num = (10, 20, 30, 40)
print(min(num))
print(max(num))  
print(sum(num))