#!/usr/bin/python

from setuptools import setup , find_packages
    
setup ( name = " eparrillae-crawler " ,
    version = " 0.1 " ,
    packages = find_packages () ,
    scripts = ['eparrillae-crawler'] ,
    install_requires = [] ,
    package_data = { 'pyeparrillae-crawler': [''] , } ,
    author = " eparrillae " ,
    author_email = " eparrillae@gmail.com " ,
    description = "  Just another Web Crawler example " ,
    license = "MIT License" ,
    keywords = " " ,
    url = " " ,
    long_description = "This is the... " ,
    download_url = " " , )

