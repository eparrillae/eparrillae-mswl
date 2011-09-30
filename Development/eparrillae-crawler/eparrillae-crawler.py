#!/usr/bin/env python

# Copyright (c) 2011 Esther Parrilla-Endrino (eparrillae@gmail.com)

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import urllib2
import argparse
from BeautifulSoup import BeautifulSoup as Soup

# === read url and depth level from the command line...

try:
    parser = argparse.ArgumentParser(description = "This is a simple web crawler written in Python")
    parser.add_argument('url', nargs = 1 , help = 'Target URL to be crawled')
    parser.add_argument('-n', '--level', type = int, default = 1 , help = 'Depth recursive level to be reached by the crawler')

    args = parser.parse_args()
    url = args.url.pop()
    level = args.level

    print "\nThe input url is: ", url
    print "\nThe input depth level is: ", level

except AttributeError:
    print "\nERROR: Input parameters are not correct, please use --help for details about script usage" 
    exit(0)

# === wget the target web page...

try:
    user_agent = " Mozilla /5.0 ( X11 ; U ; Linux x86_64 ; en - US ) AppleWebKit /534.7 ( KHTML , like Gecko ) Chrome/7.0.517.41 Safari /534.7 "
    page = urllib2.build_opener()
    page.addheaders = [('User - agent', user_agent)]
    raw_html = page.open(url).read()

    print "\n Raw HTML retrieved is: ", raw_html
 
except urllib2.URLError:
    print "\nERROR: Could not open target url, please check web site is online and available using 'wget' command!" 
    exit(0)

# === parse input html and store links recursively...

soup_code = Soup(raw_html)
links = [link ['href'] for link
                         in soup_code.findAll('a')
                         if link.has_key('href')]

print "\n The list of links is:"
for i in links:
    print i
    		 
# hacer una funcion que reciba una url y lea sus links
# la llamamos de forma recursiva, en cada paso le sumamos
# nos salimos de un bucle infinito cuando se haya alcanzado el nivel
# identamos la salida
# comprobar que las urls estan bien, quitar enlaces con javascript etc... hay que quitarlos
# comprobar que comienzan con http
