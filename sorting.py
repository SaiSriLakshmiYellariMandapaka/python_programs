
# Sorting 
sorted_key_value_list = []
for i in range(0,len(key_value_list)):
    for j in range(0,len(key_value_list) - i -1):
        if key_value_list[j][1] > key_value_list[j+1][1]:
           temp = key_value_list[j]
           key_value_list[j] = key_value_list[j+1]
           key_value_list [j+1] = temp    
sorted_key_value_list.append(key_value_list)
print('\n \n Sorted list of tuples \n \n',sorted_key_value_list)                   
print('Country with min CO2 emission',sorted_key_value_list[0][0],'\n',
'Country with max CO2 emission',sorted_key_value_list[-1][-1])
