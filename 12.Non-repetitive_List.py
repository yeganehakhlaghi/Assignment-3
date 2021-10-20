import random
nums=[]
n=int(input("Enter the length of the list:"))
for i in range(n):
    num=random.randint(0,1000)
    if num in nums:
        continue
    else:
        nums.append(num)

print(nums)