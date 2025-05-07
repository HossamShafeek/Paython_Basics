# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myFile = open("D:\Python\Files\osama.txt", "a")
myFile.truncate(5) # بيجيب خمسه ويحذف الباقي


myFile = open("D:\Python\Files\osama.txt", "a")
print(myFile.tell()) # بيجيب مكان المؤشر

myFile = open("D:\Python\Files\osama.txt", "r")
myFile.seek(11) # بينقل المؤشر 
print(myFile.read())

os.remove("D:\Python\Files\osama.txt")