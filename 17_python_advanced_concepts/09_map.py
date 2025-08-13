numbers = [1,2,4,5,6,7,8]

# def square(x):
#     return x * x

# new = list(map(square, numbers))
new = list(map(lambda x: x*x, numbers))
print(new)