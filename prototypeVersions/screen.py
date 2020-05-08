import os

listOfFiles = os.listdir("foo")
print(type(listOfFiles))

for l in listOfFiles:
	print(l)	
	print(l[-3:])
