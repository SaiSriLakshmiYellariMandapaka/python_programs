#Lists

flowers = ['Rose','Jasmine','Sunflower','Daisy','Tulip','Marigold']

print(flowers) #prints the entire list

print(flowers[0]) #prints a specific element from the  list as specified by the index

print(flowers[1:]) #prints all the elements through the list starting from index 1

print(flowers[-1]) #prints the last element in the list : negative indexing

print(flowers[2:5]) #prints elements from index  2  to 4 it doesn't include the element or item at index 5

print(flowers[:-1]) #prints all the elements from the reverse index until the first index in the list

flowers[1] = 'Lavender' #modifies the value at index 1

print(flowers[1])

print(flowers) #prints the modified list 

#-----------------------------List Functions-----------------------------------------
#print(flowers)

colors = ['Red','White','Yellow','Violet','Blue','Pink','Magenta']
flowers.extend(colors)#extend method takes a list and appends it to another list
print(flowers)

flowers.pop() #pops the last item from the list
print(flowers)

colors.append("Grey") #add individual items to the list
print(colors)

flowers.insert(1,"Lily") #inserts an item at a specific index to the list
print(flowers)

flowers.remove("Jasmine") #removes an item from the list
print(flowers)

flowers.clear() #clears the entire list and returns an empty list
print(flowers)

flowers.index("Lily") #checks whether an item is in the list or not. If it is in the list it returns the index of the item else it returns an error
print(flowers)

colors.append("Pink") #appending "Pink" color one more time
print(colors)

print(colors.count("Pink")) #counts the number of times a particular item occurs in the list.

colors.sort() #sorts the list in the ascending order.
print(colors)

numbers = [11,69,587,3,0,59,143,11,4663,14]

numbers.sort() #sorts the list in ascending order by default
print(numbers)

numbers.reverse() #reverses the list
print(numbers)

numbers1 = numbers.copy() #copies one list into another
print(numbers1)