num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))


i = max(num1 , num2)

res = 0

while ( i > 1):
	if ( (num1 % i) == 0 ) and ( (num2 % i) == 0 ):
		if res == 0:
			res = i			
	
	i -= 1
	
if res == 0:
	print("The Numbr=1")
else:
	print( "The Number is :",res)