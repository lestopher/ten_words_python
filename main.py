#!/usr/bin/env python
from lib.ten_words import TenWords
import sys

if len(sys.argv) > 1:
    fileName = sys.argv[1]
else:
    fileName = "declaration"

filePath = {
    "declaration": "data/declaration_of_independence.txt",
    "constitution": "data/constitution.txt"
}

f = open(filePath[fileName], 'rb')
data = f.read()
f.close()

tw = TenWords(data)

for word in tw.get_top_ten_words(True):
    print word
