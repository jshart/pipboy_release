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


print(createPage())
