#!/usr/bin/python

import sys
import urllib
from bs4 import BeautifulSoup

if len(sys.argv) == 1:
    print "Usage: ./bash-cli.py <bash paste id or -r for random>"
    exit();

if sys.argv[1] == "-r":
    url = "http://bash.org.pl/random"
else:
    url = "http://bash.org.pl/" + sys.argv[1]

f = urllib.urlopen(url)
html = f.read()
soup = BeautifulSoup(html, "lxml")
quote = soup.find("div", class_="quote post-content post-body")
reset = 0
if not hasattr(quote, 'contents'):
    print "Quote not found, use -r instead of quote id to choose random quote"
    exit();

for x in quote.contents:
    if reset == 1:
        reset = 0
        continue
    reset = 1
    print x.strip()
