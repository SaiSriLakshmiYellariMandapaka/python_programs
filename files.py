#program including try and exception blocks also file opening

man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken) = each_line.spilt(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)    
        except:
            pass
        data.close()        
except IOError:
    print('The datafile is missing')        
print(man)    
print(other)
try:
    man_file = open('man_data.txt','w') 
    other_file = open('other_data.txt','w')
    print(man,file = man_file)
    print(other,file = other_file)
    man_file.close()
    other_file.close()  
except IOError:
    print('File Error')
    
