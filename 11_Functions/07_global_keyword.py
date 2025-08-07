def sum(a,b):
    print("Hey I'm Summing")
    c = a + b
    global z # Please modify global z
    z = 0 # This will refer to global z and not create a local variable
    return c 

z = 5
print(sum(5,10))
print(z)