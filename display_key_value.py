
student = {
    "name": "surya",
    "age": 22,
    "course": "Python",
    "grade": "A"
}


print("Available keys:", list(student.keys()))

key = input("Enter a key to get its value: ")

if key in student:
    print(f"The value for '{key}' is: {student[key]}")
else:
    print("Key not found in the dictionary ")
