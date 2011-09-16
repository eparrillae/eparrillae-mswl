#!/usr/bin/env python

# add license text

import urllib2
import argparse
from BeautifulSoup import BeautifulSoup as Soup

# read url and depth level from the command line
# capturar la excepcion AttributeError

parser = argparse.ArgumentParser ( description = " This is a simple web crawler " )
parser.add_argument ( 'url', nargs=1 , help='target URL')
#parser.add_argument ( '-n' , '-- deep' , type=int , default=1 , help = 'how deep the craaaawl will go')
args = parser.parse_args()
url = args.url.pop()
#deep = args.deep

print "\nThe input url is: ", url
#print "\nThe depth level is: ", deep

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

print links
for i in links:
    print i
			 
# hacer una funcion que reciba una url y lea sus links
# la llamamos de forma recursiva, en cada paso le sumamos
# nos salimos de un bucle infinito cuando se haya alcanzado el nivel
# identamos la salida
