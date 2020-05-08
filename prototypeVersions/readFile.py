from os import listdir


def createLine(startStr):
   myStr=startStr
   for x in range(10):
      myStr+=str(x)

   return(myStr)

def createPage():
   myStr=""
   for x in range(5):
      myStr+=createLine("L"+str(x))+"\n"
   return(myStr)


def readFile(filename):
    f=open(filename,"r")
    
    myStr=""
    if f.mode == 'r':
        contents=f.readlines()
        for x in contents:
            #myStr+=createLine("]")+"\n"
            myStr+=x[0:10]
            #print(x[0:10])

    return(myStr)

def readDir(dir):
    directories = listdir(dir)
    for f in directories:
        print(f)
        print(readFile(dir+"/"+f))

readFile("gitNotes")
print("*** Directories ***")
readDir("UIScreens")
    
