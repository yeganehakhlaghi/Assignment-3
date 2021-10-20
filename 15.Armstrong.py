import math
number=int(input("Enter your namber:"))
num=number
A=[]
while num:
    A.append(int(num%10))
    num=int(num/10)
n=len(A)
sum=0
for nums in A:
    sum=sum+nums**n
if sum==number:
    print("yes")
else:
    print("no")