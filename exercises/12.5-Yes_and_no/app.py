theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

newList=[]
newList = list(map(lambda x: "wiki" if x == 1 else "woko" ,theBools ))

# print(1 == True)
# is_nice = True
# state = "nice" if is_nice else "not nice"
print(newList)
