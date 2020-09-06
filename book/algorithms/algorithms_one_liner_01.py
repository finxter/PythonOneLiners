# Finding Anagrams with Lambda Functions and Sorting


## One-Liner
is_anagram = lambda x1, x2: sorted(x1) == sorted(x2)

## Results
print(is_anagram("elvis", "lives"))
print(is_anagram("elvise", "livees"))
print(is_anagram("elvis", "dead"))
'''
True
True
False
'''
