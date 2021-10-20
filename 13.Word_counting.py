str=input("enter your sentence : ")
space=1
for char in str:
    if char==' ' or char == '\'':
        space+=1
    
print("The number of words is:",space)