# Palindrome Python One-Liner
phrase.find(phrase[::-1])

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

# Fibonacci Python One-Liner
fib = lambda x: x if x<2 else fib(x-1) + fib(x-2)

# Quicksort Python One-liner
lambda L: [] if L==[] else qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])

# Sieve of Eratosthenes Python One-liner
reduce((lambda r,x: r-set(range(x**2,n,x)) if (x in r) else r), range(2,int(n**0.5)), set(range(2,n)))

# Find all dividers of a number

[divider for divider in range(1, YOUR_NUMBER) if YOUR_NUMBER % divider == 0]

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
