from functools import reduce
n = [1,2,3,4,5,6,7,8]

def sum(a,b):
    return a + b

c = reduce(sum, n)
print(c)
