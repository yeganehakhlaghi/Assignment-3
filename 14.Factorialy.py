num=int(input("Enter your number:"))
fact=1
i=1
while "true":
    if fact >= num:
        break
    else:
        fact*=i
        i+=1

if fact==num:
    print("The number entered is factorial")
else:
    print("The number entered is not factorial")