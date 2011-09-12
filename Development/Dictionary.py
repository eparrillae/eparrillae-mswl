#!/usr/bin/python

# sample script in Python 
# that reads a text file line by line
# and stores some values in a dictionary
# it also reads command line parameters
# and handles exceptions
# to run the script just do: $ python Dictionary.py username

import sys

name = sys.argv[1:]

# check that the input username is not null
try: 
    if name[0] == None or name[0] == "":
    	print "No input username provided..."
except IndexError:
    print "ERROR: The input username cannot be null!" 
    exit(0)

# if input username exists, open the file for reading its contents
print "Input username is: ", name[0]
try:
    f = open("/etc/passwd")
except IOError:
    print "Error opening /etc/passwd file!" 
    exit(0)
        
userExists = 0
while 1:
    line = f.readline()
    if not line: break
    
    # check if this line corresponds to the input user
    formattedOutput = line.split( ":" )
    if name[0] == formattedOutput[0]:
    	print "The shell used by " + name[0] + " is: " + formattedOutput[6]
	
	# TODO: store the shell of the given user in a dictionary
	
	userExists = 1
	break

f.close()

# check if user exists or not in /etc/password file
if userExists == 0:
    print "ERROR: The input username is not registered on /etc/passwd file!" 
