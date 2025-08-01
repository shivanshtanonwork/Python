age = int(input("Enter your age : "))

if(age>18):
    print("You can drive")
elif(age == 18):
    print("Let's schdeule an interview")
elif(age == 0):
    print("You are just Born")
else:
    print("You cannot drive")