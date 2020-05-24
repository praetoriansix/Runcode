#!/usr/bin/env python
import sys

argsout = ' '.join(sys.argv[1:])

print(argsout)

import hashlib
hashoutput = hashlib.sha1(argsout.encode('utf-8'))
hashed = hashoutput.hexdigest()
#print(hashed)
