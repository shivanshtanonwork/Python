#Strings are immutable
# name = "Shivansh"

# name[1] = "i" # Can't do this

s = " hello Python "
a = len(s)
print(a)
# print(s.upper(), s)
# Changing Case
print(s.lower())
print(s.upper())
print(s.capitalize()) # converts the 1st char of the string to capital and rest in lower case
print(s.title())

# Removing Whitespace
print(s.strip())
print(s.lstrip())
print(s.rstrip())

#Finding and Replacing
text = "Python is fun is fun is fun"
print(text.find("fun")) # O/p 10 returns index of 1st occurence
print(text.replace("fun", "awesome")) # returns new string with all string replaced

#Splitting and Joining
fruits = "Apples,Bananas,Pineapples"
print(fruits.split(",")) #split fnx will convert it into a list 
print("-".join(['Apples', 'Bananas', 'Pineapples']))

#Checking String Properties
eg = "Python1503"
print(eg.isalpha()) #False
print(eg.isdigit()) #False
print(eg.isalnum()) #True
print(eg.isspace()) #False