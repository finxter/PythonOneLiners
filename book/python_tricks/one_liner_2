# Using List Comprehension to Find Words with High Information Value


## Data
text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

## One-Liner
w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]

## Result
print(w)
'''
[[], ['Call', 'Ishmael.', 'Some', 'years', 'never', 'mind', 'long', 'precisely', 'having'], 
['little', 'money', 'purse,', 'nothing', 'particular', 'interest'], 
['shore,', 'thought', 'would', 'sail', 'about', 'little', 'watery', 'part'], 
['world.', 'have', 'driving', 'spleen,', 'regulating'], ['circulation.', 'Moby', 'Dick']]
'''
