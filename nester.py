#List of lists
movies = ['bahubali','omg','detective','oh! baby',['Namaste london',['om shanti om','brothers','24','arjun','bommarillu']]]
print(movies[4][1][0]) #printing a data item in the inner most list


#trying to print all the data items in the list of lists using 'for' loop , 'if' conditional statement and isinstance() BIF

for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            if isinstance(nested_item,list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)        
    else:
        print(each_item)            

#Creating a function to stop writing numerous lines of code as list of lists keep on increasing

# Defining the function
def print_lol(the_list):

    for each_item in movies:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)    

print_lol(movies) #Invoking the function

#Using range() BIF,introducing another argument 'level' to control how many tab-stops and  printing tab stops
def print_lol(the_list,level):

    for each_item in movies:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            for tab_stops in range(level):
                print("\t",end = '')
            print(each_item)    

print_lol(movies)

data = open('sketch.txt')
#To control indentation level

def print_lol(the_list,indent = False,level =0):

    for each_item in movies:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1)
        else:
            if indent:
            for tab_stops in range(level):
                print("\t",end = '')
            print(each_item)    

print_lol(movies)
print_lol(movies,True)
print_lol(movies,True,4)


# Using sys.stdout inorder to avoid print() BIF and this print_lol would be invoked for performing this action


def print_lol(the_list,indent = False,level =0,fh=sys.stdout):

    for each_item in movies:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fh)
        else:
            if indent:
            for tab_stops in range(level):
                print("\t",end = '',file=fh)
            print(each_item,file=fh)    





