#!/usr/bin/python

# sample script in Python 
# that reads a text file line by line
# to run the script just do: $ python FileRead.py

# open the file for reading its contents
f = open("/etc/passwd")
while 1:
    line = f.readline()
    if not line: break
    
    #process line to format the output
    formattedOutput = line.split( ":" )
    print formattedOutput[0] + " -> " + formattedOutput[6]

f.close()
