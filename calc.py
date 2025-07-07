a=int(input("Enter the 1st input:"))
b=int(input("enter the 2nd input:"))
c=int(input("enter the preferrable calculation you want to perform on the two numbers:\n1.Add\n2.subtarct\n3.Multiply\n4.Divide\n5.Floor Divide\n6.Modulo\n7.Exponentiation\n::"))
if c == 1:
	print("Sum of ",a," + ",b," = ",a+b)
elif c == 2:
	if a > b:
		print("Difference of ",a," and ",b," = ",a-b)
	else:
		print("Difference of ",a," and ",b," = ",b-a)
elif c == 3:
	print("Product of ",a," and ",b," = ",a*b)
elif c == 4:
	print("Quotient of ",a," and ",b," = ",a/b)
elif c == 5:
	print("Floor Quotient of ",a," and ",b," = ",abs(a//b))
else:
	print("enter a valid option")
	
