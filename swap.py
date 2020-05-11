#swapping of 2 numbers using a temp variable
a = int(input('Enter the first number'))
b = int(input('Enter the second number'))

print('Before swapping a is:',a)
print('Before swapping b is:',b)
temp = 0

temp = a
a = b
b = temp

print('After swapping a is:',a)
print('After swapping b is:',b)
