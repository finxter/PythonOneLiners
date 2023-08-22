# Palindrome Python One-Liner
phrase.find(phrase[::-1])

# print N numbers Python One-Liner
print(*range(N))
# Swap Two Variables Python One-Liner
a, b = b, a

# Sum Over Every Other Value Python One-Liner
sum(stock_prices[::2])

#To input space separated integers in a list
lis = list(map(int, input().split()))

# Read File Python One-Liner
[line.strip() for line in open(filename)]

# Factorial Python One-Liner
reduce(lambda x, y: x * y, range(1, n+1))

# Performance Profiling Python One-Liner
python -m cProfile foo.py

# Superset Python One-Liner
lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])

# Generate Random Password
from random import choice; print(''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)') for i in range(10)]))

# Generate Random Password without use of semicolon
print(''.join([__import__("random").choice('abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)') for _ in range(10)]))

# Fibonacci Python One-Liner
fib = lambda x: x if x<2 else fib(x-1) + fib(x-2)

# Quicksort Python One-liner
lambda L: [] if L==[] else qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])

# Sieve of Eratosthenes Python One-liner
reduce((lambda r,x: r-set(range(x**2,n,x)) if (x in r) else r), range(2,int(n**0.5)), set(range(2,n)))

# Find all dividers of a number

[divider for divider in range(1, YOUR_NUMBER) if YOUR_NUMBER % divider == 0]

# vigenere cipher usage: vigenere(message, key, mode) mode is e for encrypt and d for decrypt, only works for Uppercase letters
vigenere = lambda message, key, mode: ((lambda k_length=len(key), k_int=[ord(i) for i in key], message_int=[ord(i) for i in message]: "".join([chr(((message_int[i] + k_int[i % k_length]) % 26) + 65) for i in range(len(message_int))]))() if (mode.lower() == "e") else ((lambda k_length=len(key), k_int=[ord(i) for i in key], message_int=[ord(i) for i in message]: "".join([chr(((message_int[i] - k_int[i % k_length]) % 26) + 65) for i in range(len(message_int))]))() if mode.lower() == "d" else ""))

# IMPORTLESS sha256 one-liner, usage: sha256(b"data")
sha256 = lambda data: (type("SHAConstructor", (object, ) , {'__init__': lambda self, data, **kwargs: [[setattr(self, key, value) for key, value in zip(["data", "hashes", "round_constants", "preprocessed_data"], [data, [0x6A09E667,0xBB67AE85,0x3C6EF372,0xA54FF53A,0x510E527F,0x9B05688C,0x1F83D9AB,0x5BE0CD19,], [0x428A2F98,0x71374491,0xB5C0FBCF,0xE9B5DBA5,0x3956C25B,0x59F111F1,0x923F82A4,0xAB1C5ED5,0xD807AA98,0x12835B01,0x243185BE,0x550C7DC3,0x72BE5D74,0x80DEB1FE,0x9BDC06A7,0xC19BF174,0xE49B69C1,0xEFBE4786,0x0FC19DC6,0x240CA1CC,0x2DE92C6F,0x4A7484AA,0x5CB0A9DC,0x76F988DA,0x983E5152,0xA831C66D,0xB00327C8,0xBF597FC7,0xC6E00BF3,0xD5A79147,0x06CA6351,0x14292967,0x27B70A85,0x2E1B2138,0x4D2C6DFC,0x53380D13,0x650A7354,0x766A0ABB,0x81C2C92E,0x92722C85,0xA2BFE8A1,0xA81A664B,0xC24B8B70,0xC76C51A3,0xD192E819,0xD6990624,0xF40E3585,0x106AA070,0x19A4C116,0x1E376C08,0x2748774C,0x34B0BCB5,0x391C0CB3,0x4ED8AA4A,0x5B9CCA4F,0x682E6FF3,0x748F82EE,0x78A5636F,0x84C87814,0x8CC70208,0x90BEFFFA,0xA4506CEB,0xBEF9A3F7,0xC67178F2,], self.preprocessing(data)])][0], self.finalhash()][0],'preprocessing': lambda self, data: data + b"\x80" + (b"\x00" * (63 - (len(data) + 8) % 64)) + __import__("struct").pack(">Q", (len(data) * 8)),'ror': lambda self, value, rotations: 0xFFFFFFFF & (value << (32 - rotations)) | (value >> rotations),'finalhash': lambda self: [func() for func in [lambda: setattr(self, "blocks", [self.preprocessed_data[x : x + 64] for x in range(0, len(self.preprocessed_data), 64)]),lambda: [[setattr(self, "words", list(__import__("struct").unpack(">16L", block))), setattr(self, "words", self.words + ([0] * 48)), [setattr(self, c, v) for c,v in zip(list("abcdefgh"), self.hashes)], [[(self.zero(index) if index > 15 else None), setattr(self, "S1", self.ror(self.e, 6) ^ self.ror(self.e, 11) ^ self.ror(self.e, 25)), setattr(self, "ch", (self.e & self.f) ^ ((~self.e & (0xFFFFFFFF)) & self.g)), setattr(self, "temp1", (self.h + self.S1 + self.ch + self.round_constants[index] + self.words[index]) % 0x100000000), setattr(self, "S0", self.ror(self.a, 2) ^ self.ror(self.a, 13) ^ self.ror(self.a, 22)), setattr(self, "maj", (self.a & self.b) ^ (self.a & self.c) ^ (self.b & self.c)), setattr(self, "temp2", (self.S0 + self.maj) % 0x100000000), [setattr(self, f, m) for f, m in zip(list("hgfedcba"), [self.g, self.f, self.e, ((self.d + self.temp1) % 0x100000000), self.c, self.b, self.a, ((self.temp1 + self.temp2) % 0x100000000),])]] for index in range(0,64)], self.final()] for block in self.blocks],lambda: setattr(self, "hash", "".join([hex(value)[2:].zfill(8) for value in self.hashes])),lambda: self.hash]][-1],'final': lambda self: [setattr(self, "mutated_hash_values", [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h]), setattr(self, "hashes", [((element + self.mutated_hash_values[index]) % 0x100000000)for index, element in enumerate(self.hashes)])],'zero': lambda self, index: [setattr(self, "s0", (self.ror(self.words[index - 15], 7) ^ self.ror(self.words[index - 15], 18) ^ (self.words[index - 15] >> 3))), setattr(self, "s1", (self.ror(self.words[index - 2], 17)^ self.ror(self.words[index - 2], 19)^ (self.words[index - 2] >> 10))), self.words.__setitem__(index, (self.words[index - 16] + self.s0 + self.words[index - 7] + self.s1) % 0x100000000),], '__repr__': lambda self: self.hash, '__str__': lambda self: self.hash}))(data)

# print a love emoji with a give name, here it prints my username (Zenoftech) https://github.com/zenoftech
print('\n'.join([''.join([('Zenoftech'[(x-y)%9 ]if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ') for x in range(-30,30 )])for y in range(15, -15, -1)]))

# Get back rot-13 version of text you enter
(lambda x, a = "abcdefghijklmnopqrstuvwxyz", b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ": "".join([a[a.index(x[i]) - 13] if x[i] in a else b[b.index(x[i]) - 13] if x[i] in b else x[i] for i in range(len(x))]))(input("Enter text: "))

# Replace banned words in string with a special character
lambda text, words, char = '*': [text := text.replace(word, char * len(word)) for word in words][-1]

# General One-Liner Commands From https://gist.github.com/craigls/2712084
'''
Some useful Python one-liners taken from http://www.reddit.com/r/Python/comments/fofan/suggestion_for_a_python_blogger_figure_out_what/

All modules listed are part of the standard library and should work with Python 2.6+

How to use:

    $ python -m [module] [arguments]

calendar - does default to displaying a yearly calendar, but it has a bunch of options (args are year or year month, options are HTML output, calendar locale, encoding, and some type-specific stuff, see python -m calendar -h)
cgi, dumps a bunch of information as HTML to stdout
CGIHTTPRequestHandler - same as SimpleHTTPServer except via the CGIHTTPRequestHandler: it will executes scripts it recognizes as CGI, instead of just sending them over (has not survived the transition to Python 3)
compileall - compiles a tree of Python files to bytecode, has a bunch of options. Does not compile to stripped files (pyo)
cProfiler - runs the provided script file (argument) under cProfiler
dis disassembles a python script
doctest - runs doctests on the provided files (which can be python scripts or doctest files)
encodings.rot_13 - rot13 encodes stdin to stdout (has not survived the transition to Python 3)
filecmp - directory entry comparison tool
fileinput - some kind of ghetto pseudo-annotate. No idea what use that thing might be of
formatter - reformats the provided file argument (or stdin) to stdout: 80c paragraphs &etc
ftplib - ghetto FTP client
gzip - ghetto gzip (or gunzip with -d), can only compress and decompress, does not delete the archive file
htmllib - strips HTML tags off of an HTML file
ifc - dumps some info about the provided aiff file (if given two paths, also copies path1 to path2)
imaplib - ghetto IMAP client
json.tool - pretty prints JSON
locale - displays current locale information
mimify - converts (mail) messages to and from MIME format
modulefinder - lists the modules imported by the provided script argument, and their location
pdb - automatically enters PDB post-mortem mode if the script crashes
platform - displays the platform string
poplib - dumps a bunch of info on a POP mailbox
profile - see cProfile
pstats - opens a statistics browser (for profile files)
pydoc - same as the pydoc command
quopri / uu  binhex / base64 - encode / decode - quoted-Printable / UUEncoded content.
shlex - displays tokenization result of the provided file argument (one token per line prefixed with Token:)
SimpleHTTPServer - serve the current directory over HTTP on port 8080
SimpleXMLRPCServer - XMLRPC server for power and addition
smtpd - SMTP proxy
telnetlib - telnet client
timeit - command line profiling interface
tokenize - dumps tokenization result of a Python file
urllib - fetches a url
webbrowser - opens provided URL in your default web browser (options: in a new window, in a new tab)
whichdb - tries to guess which db package (for db format nobody cares about) can be used to read a db file
'''
