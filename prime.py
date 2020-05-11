#Program to check whether the given number is prime or not
num = int(input("enter a number: "))
 
for i in range(2, num):
	if num % i  == 0:
		print(num,"not prime number")
		break
else:
	print(num,"prime number")
