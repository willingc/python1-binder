#!/usr/local/bin/python

import sys

print 'Check out the Python 1.0 modules:\n'
print sys.builtin_module_names

print 'Hello world from Python 1.0.'
print 'Computer Programming for Everyone'
print 'Thank you GvR!'

my_number = 1.0
my_string = "Monty Python's Flying Circus"
dir()
print __name__

f = lambda a, b, c: a + b + c
print f(1, 2, 3)

