#!/usr/bin/python

import pypandoc

try:
    rst = pypandoc.convert("README.md", "rst")
    f = open("README.txt","w")
    f.write(rst)
except:
    sys.stderr.write('Error converting README from markdown to restructuredText')
    sys.exit(1)
