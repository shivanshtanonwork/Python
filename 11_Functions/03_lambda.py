square = lambda x : x*x
print(square(9))

'''
As good as writing 
def sum(a+b):
    return a + b
'''

numbers = [1,2,3,4,5]
sqaured = list(map(lambda x:x**2, numbers))
print(sqaured)