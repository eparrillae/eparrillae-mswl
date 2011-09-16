#!/usr/bin/python

from setuptools import setup , find_packages
    
setup ( name = " eparrillae-crawler " ,
    version = " 1.0 " ,
    packages = find_packages () ,
    scripts = ['eparrillae-crawler'] ,
    install_requires = [] ,
    package_data = { 'pyeparrillae-crawler': [''] , } ,
    author = " eparrillae " ,
    author_email = " eparrillae@gmail.com " ,
    description = "  Just another Web Crawler example " ,
    license = "MIT License http://www.opensource.org/licenses/mit-license.php" ,
    keywords = " mswl, web, crawler, python, MIT" ,
    url = " " ,
    long_description = "This is the web crawler script for the Development subjet of the MSWL  " ,
    download_url = " git://github.com/eparrillae/eparrillae-mswl.git " , )

