""" 
Drag The vbs trojan to the script to get the binary
"""

import re, base64
from sys import argv

vbs = open(argv[1], "rb").read()
encoded_code_splited = re.findall('FFwflY.*? = \"(.*?)\"', vbs)
print "Lines:", len(encoded_code_splited)
encoded_code = reduce(lambda x,y:x+y, encoded_code_splited)
code = base64.b64decode(encoded_code)
print "Start of File:", code[:50]
print "Turn off windows Defender!"

open(argv[1] + ".exe.dontrun", "wb").write(code)



