#!/usr/bin/env python
import hashlib

print("Hello, World!")


stringsha1 = hashlib.sha1(b"Hello, World!")
hex_dig = stringsha1.hexdigest()
#print(hex_dig)