#!/usr/bin/python

# first sample script in Python
# to run the script just do: $python HelloWorld.py

print "Voy a leer el fichero!"

# open the file for reading its contents
f = open("/etc/passwd")
while 1:
    line = f.readline()
    if not line: break
    
    #process line to format the output
    formattedOutput = line.split( ":" )
    print formattedOutput[0] + " -> " + formattedOutput[6]

f.close()
