'''
0 1 1 2 3 5 8 13
0 1 2 3 4 5 6......

fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
fib(4) = fib(2) + fib(3)
fib(n) = fib(n-2) + fib(n-1)
'''

def fib(n):
    # Base case of recursion
    if(n == 0 or n == 1):
        return n
    
    return fib(n-2) + fib(n-1)

print(fib(6))

#must have base case to avoid infinite recursion as it also starts taking -ive values
# used in algo like fibonacci, tree traversals
'''
fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
fib(0) + fib(1) + fib(3) + fib(5)
0 + 1 + fib(1) + fib(2) + fib(3) + fib(4)
0 + 1 + 1 + fib(0) + fib(1) + fib(1) + fib(2) + fib(4)
0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(2) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(2) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(1) + fib(2) 
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1) 
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 
'''

# with loop
def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b=b,a+b  # means a=b b=a+b will learn this in tuple
    return a
print(fib(4))
