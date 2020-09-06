# Finding Nonsecure HTTP URLs


## Dependencies
import re

## Data
article = '''
The algorithm has important practical applications
http://blog.finxter.com/applications/
in many basic data structures such as sets, trees,
dictionaries, bags, bag trees, bag dictionaries,
hash sets, https://blog.finxter.com/sets-in-python/
hash tables, maps, and arrays. http://blog.finxter.com/
http://not-a-valid-url
http:/bla.ba.com
http://bo.bo.bo.bo.bo.bo/
http://bo.bo.bo.bo.bo.bo/333483--33343-/
'''

## One-Liner
stale_links = re.findall('http://[a-z0-9_\-.]+\.[a-z0-9_\-/]+', article)

## Results
print(stale_links)
'''
['http://blog.finxter.com/applications/', 'http://blog.finxter.com/',
'http://bo.bo.bo.bo.bo.bo/', 'http://bo.bo.bo.bo.bo.bo/333483--33343-/']
'''
