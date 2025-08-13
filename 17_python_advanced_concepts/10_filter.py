# def is_greater_than_9(x):
#     if x > 9:
#         return True
#     else:
#         return False
    
a = [1, 11, 5, 99, 22, 81, 8]

# new = list(filter(is_greater_than_9, a))
new = list(filter(lambda x: x>9, a))
print(new)