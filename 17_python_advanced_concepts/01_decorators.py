# A decorator is a func that - takes a function, creates a new funtion inside its body (wrapper). Then it returns that new function.

def decorator(func):
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("I have executed this function...")
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()
# f = decorator(say_hello)
# f()

'''
f will look like this 
def f():
    print("I am about to execute a function...")
    print("Hello")
    print("I have executed this function...")

'''