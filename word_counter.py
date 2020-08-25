#Word Counter in python
import re #Regular Expression module
from collections import Counter

def count_words(path):
    with open(path) as File:
        all_words = re.findall(r"[0-9a-zA-Z-')+",file.read())
        # re.findall := The string is scanned left-to-right, and matches are returned in the order found.
        all_words = [word.upper() for word in all_words]
        
        word_counts = Counter()
        for word in all_words:
            word_counts[word] += 1
            
print('\n Top 20 words: ')            

for word in word_counts.most_common(10):
                print(word[0],'\t',word[1])

if __name__ == '__main__':
    count_words("/home/srilakshmi/Documents/python_programs/Other")