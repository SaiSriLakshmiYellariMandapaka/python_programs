# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
from datetime import datetime
name = input("Enter a name: ")
age = int(input("Enter age: "))
current_year = datetime.now().year
print("Age when " + name + " will be 100 years old is : " + str(current_year-age+100))
