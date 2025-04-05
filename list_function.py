#List functiuon

fruits = ["mango", "orange", "cherry"]
print(fruits)

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

fruits = ["apple", "papaya"]
add_fruits = ["cherry", "grape"]
fruits.extend(add_fruits)
print(fruits)

fruits = ["apple", "banana"]
fruits.insert(1, "guava")  
print(fruits)

fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)

fruits = ["apple", "banana", "cherry"]
last_fruit = fruits.pop()  
print(fruits)  
print(last_fruit)

fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))

num = [1, 2, 3, 2, 2, 4]
print(num.count(2))

num= [4, 2, 8, 1]
num.sort()
print(num)


num = [4, 2, 8, 1]
sorted_num = sorted(num)
print(sorted_num) 
print(num) 


fruits = ["apple", "mango", "guava"]
fruits.reverse()
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

num = [4, 2, 8, 1]
print(max(num))  
print(min(num)) 

num = [1, 2, 3, 4]
print(sum(num))
