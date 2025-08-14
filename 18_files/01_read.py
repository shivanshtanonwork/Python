try:
    f = open("shivansh.txt", "r")

    content = f.read()
    print(content)
    f.close()

except FileNotFoundError:
    print("File not found !")


with open("shivansh.txt", "r") as f:
    cont = f.read()
    print(cont)
    
