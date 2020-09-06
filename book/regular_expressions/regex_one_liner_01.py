# Finding Basic Textual Patterns in Strings


## Dependencies
import re

## Data
text = 'peter piper picked a peck of pickled peppers'

## One-Liner
result = re.findall('p.*?e.*?r', text)

## Result
print(result)
'''
['peter', 'piper', 'picked a peck of pickled pepper']
'''
