#Calculator program
#addition function
def add(x,y):
    return x + y

#subtraction function
def sub(x,y):
    return x - y

#multiplication function
def mul(x,y):
    return x * y

#division function
def div(x,y):
    return x / y

print('select the option:')

print('1.Addition')

print('2.Subtraction')

print('3.Multiplication')

print('4.Division')


option = input('Select option 1 or 2 or 3 or 4 :')

n1 = float(input('enter number 1:'))

n2 = float(input('enter number 2:'))

if option == 1:
    print(add(n1,n2))

elif option == 2:
    print(sub(n1,n2))

elif option == 3:
    print(mul(n1,n2))

elif option == 4:
    print(div(n1,n2))

else :
    print('Invalid option')
