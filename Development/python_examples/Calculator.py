#!/usr/bin/python

# sample calculator script in Python 
# to run the script just do: $ python Calculator.py [number operator number]

import sys

params = sys.argv[1:]

try: 
    # cast arguments to float
    first    = float(params[0])
    operator = params[1]
    second   = float(params[2])
    print "\nThe operation to be performed is:"
    print params[0], params[1], params[2]
	
    # determine which operation should be performed
    if params[1] == "+":
    	print params[0], params[1], params[2], "=", first + second
    elif params[1] == "-":
    	print params[0], params[1], params[2], "=", first - second
    elif params[1] == "*":
    	print params[0], params[1], params[2], "=", first * second
    elif params[1] == "/":
    	print params[0], params[1], params[2], "=", first / second
    else:
    	print "\nERROR: Operator does not exists!"

# raise exception in case input args are incorrect...
except IndexError:
    print "\nERROR: Input parameters are incorrect!" 
    print "\nPlease provide: [number operator number]" 
    exit(0)
