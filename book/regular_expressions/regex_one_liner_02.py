# Writing Your First Web Scraper with Regular Expressions


## Dependencies
import re

## Data
text_1 = "crypto-bot that is trading Bitcoin and other currencies"
text_2 = "cryptographic encryption methods that can be cracked easily with quantum computers"

## One-Liner
pattern = re.compile("crypto(.{1,30})coin")

## Result
print(pattern.match(text_1))
print(pattern.match(text_2))
'''
<re.Match object; span=(0, 34), match='crypto-bot that is trading Bitcoin'>
None
'''
