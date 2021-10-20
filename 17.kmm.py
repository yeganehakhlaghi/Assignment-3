max = 1;
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
for num in range(1,(num1+1)):
    if num1 % num == 0 and num2 % num == 0:
        if num > max:
            max = num
#print("max",max)
kmm = num1 * num2 / max
print("kmm =",int(kmm))