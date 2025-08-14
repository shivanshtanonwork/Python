import os

a= os.listdir("dir")
print(a)
print(os.getcwd())
print(os.path.exists("Shivansh"))
os.remove("dir/sample_file.txt")
# os.rmdir("") only removes empty directories
