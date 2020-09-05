# Using Slice Assignment to Correct Corrupted Lists


## Data
visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
            'Safari', 'corrupted', 'Safari', 'corrupted',
            'Chrome', 'corrupted', 'Firefox', 'corrupted']

## One-Liner
visitors[1::2] = visitors[::2]

## Result
print(visitors)
'''
['Firefox', 'Firefox', 'Chrome', 'Chrome', 'Safari', 'Safari',
'Safari', 'Safari', 'Chrome', 'Chrome', 'Firefox', 'Firefox']
'''
