#!/usr/bin/python

# sample script in Python 
# that reads a text file line by line
# and stores some values in a dictionary
# it also reads command line parameters
# and handles exceptions
# to run the script just do: $ python Dictionary.py username

import sys

# check that the input username is not null
name = sys.argv[1:]
try: 
    if name[0] == None or name[0] == "":
    	print "No input username provided..."
except IndexError:
    print "\nERROR: The input username cannot be null!" 
    exit(0)

# if input username exists, open the file for reading its contents
print "\nInput username is: ", name[0]
try:
    f = open("/etc/passwd")
except IOError:
    print "\nERROR opening /etc/passwd file!" 
    exit(0)
        
userExists = 0
firstLine = 1
while 1:
    line = f.readline()
    if not line: break

    # store the shell of the given user in a dictionary
    formattedOutput = line.split( ":" )
    # check if this is the first iteration
    if firstLine == 1:
        d = {formattedOutput[0]: formattedOutput[6]} 
	firstLine = 0
    else:
        d[formattedOutput[0]] = formattedOutput[6]
    
    # check if this line corresponds to the input user
    if name[0] == formattedOutput[0]:
    	print "\nThe shell used by " + name[0] + " is: " + formattedOutput[6] 
	userExists = 1

f.close()

# print the values inserted in the dictionary
print "\nThe values in the dictionary are: " 
print d

# check if user exists or not in /etc/password file
if userExists == 0:
    print "\nERROR: The input username is not registered on /etc/passwd file!" 
