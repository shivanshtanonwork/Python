# String Formatting
template = "Dear {}, You are awesome. Take this {}$ bag."

a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c1 = 300

# s1 = template.format(a,a1)
# print(s1)

print(f"{a} you are awesome and take this {a1}$ bag")
print(f"{b} you are awesome and take this {b1}$ bag")
print(f"{c} you are awesome and take this {c1}$ bag")

# ord() and chr() - Character Encoding
print(ord('A')) # Output: 65
print(chr(65)) # Output: 'A'
