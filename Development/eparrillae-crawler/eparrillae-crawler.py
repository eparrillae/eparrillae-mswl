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

# Run example: $./eparrillae-crawler.py -n 2 http://www.google.com

import urllib2
import argparse
from BeautifulSoup import BeautifulSoup as Soup

#
# method for printing in the stdout the list of urls 
# and saving them into a file
#
def printAndSaveUrls(l):
    
    print "\nThe list of links processed is: \n"
    
    try:
        f = open('./eparrillae-crawler.output','w')
        for i in l:
            print(i)
            f.write(i)
            f.write("\n")
        f.close()
        
    except IOError:
        print "\nERROR: Could write to file the list of urls retrieved!" 
        exit(0)
    return

#
# recursive method for navigating through the urls
#
def processUrl(url, level, counter):   

    totalLinks = 0
    urlList.append(counter * " " + url)
    while counter < level:

        # wget the target web page...
        user_agent = " Mozilla /5.0 ( X11 ; U ; Linux x86_64 ; en - US ) AppleWebKit /534.7 ( KHTML , like Gecko ) Chrome/7.0.517.41 Safari /534.7 "
        page = urllib2.build_opener()
        page.addheaders = [('User - agent', user_agent)]
        raw_html = page.open(url).read()
        
        # get the links in this web page...
        counter += 1
        soup_code = Soup(raw_html)
        links = [link ['href'] for link in soup_code.findAll('a')
        if link.has_key('href')]
        for x in links:
            totalLinks += 1
            # absolute paths...
            if x.startswith("http") | x.startswith("https"): 
                processUrl(x, level, counter)
            # incomplete paths...
            else:
                if x.startswith("www"): 
                    absurl = "http://" + x
                    processUrl(absurl, level, counter)
                # relative paths...
                else:
                    absurl = url + x
                    processUrl(absurl, level, counter)
    return totalLinks

##
# Main
#
##

# === read url and depth level from the command line...
try:
    parser = argparse.ArgumentParser(description = "This is my web crawler written in Python for the MSWL")
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

# === parse input html and store links in a list...
try:
    urlList = []
    total = processUrl(url, level, 1)
    print "\nThe total amount of links processed is: ", total
    printAndSaveUrls(urlList)
    
except urllib2.URLError:
    print "\nERROR: Could not open target url, please check web site is online and available using 'wget' command!" 
    exit(0)



    		 
