'''
Two types of modules in python:

1) Built in Modules - math, os , time, sys etc
 - list of built in modules https://docs.python.org/3/py-modindex.html

2) External modules - written by us or installed using utility called pip
'''

import math
# import os
import mymodule
import requests

print(math.sqrt(16))
# os.abort()
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)