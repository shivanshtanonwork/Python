# while True:
#     try:
#         a = int(input("Enter no. 1: "))
#         b = int(input("Enter no. 2: "))
#         print(f"The division is {a / b}")

#     except ValueError:
#         print("Please dont perform bad typecast")

#     except ZeroDivisionError:
#         print("Hey don't divide by 0")
#     except Exception as e: 
#         print("Some Error Occurred!", e)

a = int(input("Enter no. 1: "))
b = int(input("Enter no. 2: "))
if b == 0:
    raise ValueError("Please dont divide by 0")
print(f"The division is {a/b}")