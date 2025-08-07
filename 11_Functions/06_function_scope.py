def sum(a,b):
    # a and b are local variables i.e can only be accessed inside fnx
    c = a + b
    z = 1 # It creates local variable called z which is destroyed after this function returns
    return c

z = 8 # z is a global variable can be accessed anywhere 
print(sum(4,6))
print(z)
#function only keeps variables unitl it returns after that it deletes. 