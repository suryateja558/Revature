n = int(input("Enter the number of terms: "))

a, b = 0, 1 

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
