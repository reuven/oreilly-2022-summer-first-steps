# In this module, write a function, count_vowels, which takes a string and retuns an integer.

#     The string will be text
#     The integer will be the number of vowels in that text.

# This means that your function can be accessed by import vowels and then running vowels.count_vowels on a string.
# From outside of the module (i.e., in Jupyter or a separate program), import values and run vowels.count_vowels.

def count_vowels(s):
    total = 0
    
    for one_character in s.lower():  # lowercase the string, to match capital vowels
        if one_character in 'aeiou':
            total += 1
            
    return total