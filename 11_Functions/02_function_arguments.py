# Default and positional arguments
def add(a,b,plus=10):
    return a+b+plus

print(add(5,10))
print(add(5,10,20))

# Keyword Arguments
def student(name,age):
    print(f"Name: {name}, Age: {age}")

student(age=26, name="Shivansh")
