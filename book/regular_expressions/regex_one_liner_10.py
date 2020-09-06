# Modifying Regex Patterns in a Multiline String


## Dependencies
import re

## Data
text = '''
Alice Wonderland married John Doe.
The new name of former 'Alice Wonderland' is Alice Doe.
Alice Wonderland replaces her old name 'Wonderland' with her new name 'Doe'.
Alice's sister Jane Wonderland still keeps her old name.
'''

## One-Liner
updated_text = re.sub("Alice Wonderland(?!')", 'Alice Doe', text)

## Result
print(updated_text)
'''

Alice Doe married John Doe.
The new name of former 'Alice Wonderland' is Alice Doe.
Alice Doe replaces her old name 'Wonderland' with her new name 'Doe'.
Alice's sister Jane Wonderland still keeps her old name.


'''
