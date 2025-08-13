# args collect all the arguments and returns items as tuples 

def sum(*args):
    #args will be a tuple of all the values passed to sum
    total = 0
    for item in args:
        total += item
    return total

print(sum(10,5,11))