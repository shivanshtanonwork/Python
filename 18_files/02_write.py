# Write to a file called Vidu.txt.
# It should contain data about Vidushi Choubey

f = open("vidu.txt", "w")

string = '''
Vidushi Choubey is a lovely girl. She lives in Pune and he works with Python
Her favorite package is Pandas
'''

f.write(string)

f.close()