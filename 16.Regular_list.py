f=1
list=[]
n=int(input("Enter the number of members in your list:"))
for i in range(n):
    num=int(input())
    list.append(num)
print(list)
ind=1
for j in range(n-1):
    if list[j] <= list[ind]:
        ind+=1
    else:
        f=0
        print("no")
        break
if f==1:
    print("yes")

