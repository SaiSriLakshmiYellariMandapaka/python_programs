#Rewriting code without finally suite by making use of 'with' statement

try:
    with open('man_data.txt','w') as man_file,open('other_data.txt','w') as other_file:
         print(man,file = man_file)
         print(other,file=other_file)
except IOError as err:
       print('File wrror'+str(err))
