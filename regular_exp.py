#Regular expressions module : his module provides regular expression matching operations

import re
string  = "'I AM NOT YELLING'.she Said. Though we knew it was not to be true."
print(string)
#Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl.

new = re.sub('[A-Z]','',string) #Removes all capital letters
print(new)

new = re.sub('[a-z]','',string) #Removes all small letters
print(new)

new = re.sub('[.,\']','',string) #Removes special characters
print(new)

new = re.sub('[.,\'a-zA-Z]','',string) #Removes capital,small letters and special characters.
print(new)

new = re.sub('[.,\'A-Z+" "]','',string) #Removes small letters,special characters and spaces.
print(new)

string = string + "664676856565656 -996 4444"
new = re.sub('[^0-9]','',string) #Removes non-numbers from the string
print(new)