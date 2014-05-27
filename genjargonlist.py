#!/usr/bin/env python

import urllib
from bs4 import BeautifulSoup

class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) "\
              "Gecko/20100101 Firefox/25.0"
              
urllib._urlopener = AppURLopener()
doc = BeautifulSoup(urllib.urlopen('http://www.noslang.com/dictionary/full/')\
                          .read())
for abbr in doc.find_all('abbr'):
    print abbr.text