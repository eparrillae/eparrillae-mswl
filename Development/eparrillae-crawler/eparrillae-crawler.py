#!/usr/bin/env python

# add license text

import urllib2
import sys
from BeautifulSoup import BeautifulSoup as Soup

# read url from the command line

args = sys.argv[1:]

try: 
    #url ="http://www.google.com"
    url = args[0]
    print "\nInput url is: ", url
except IndexError:
    print "\nERROR: The input url cannot be null!" 
    exit(0)

# wget the web page

user_agent = " Mozilla /5.0 ( X11 ; U ; Linux x86_64 ; en - US ) AppleWebKit /534.7 ( KHTML , like Gecko ) Chrome/7.0.517.41 Safari /534.7 "
page = urllib2 . build_opener ()
page . addheaders = [( 'User - agent' , user_agent ) ]
raw_html = page . open ( url ) . read ()

print "\n Raw HTML retrieved is: ", raw_html

# parse input html and store links

soup_code = Soup ( raw_html )
links = [ link [ 'href'] for link
                         in soup_code . findAll ( 'a')
                         if link . has_key ( 'href') ]
			 
print "This is the list of links: ", links

