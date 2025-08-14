# Append to an existing file shivansh.txt 
# It should add data about Shivansh Tandon's Hometown


f = open("shivansh.txt", "a")

string = '''
Shivansh is initially lived in Jabalpur, M.P.
He is a Full stack developer
'''

f.write(string)

f.close()