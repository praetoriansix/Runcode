#!/usr/bin/env python
import sys

listonumbers = sys.argv[1]

with open (listonumbers, 'r') as numlist:
    listo = numlist.readlines()
    for line in listo:
        nums = line.split()
        n1 = int(nums[0].strip())
        n2 = int(nums[1].strip())
        if n1 != 0:
            if n2 > 0:
                for num in range(1, n2+1):
                    if num % n1 == 0:
                        print(num)
            if n2 < 0:
                for num in range(1, n2-1, -1):
                    if num % n1 == 0:
                        if num < 0:
                            print(num)
        print()
        
        
        
        #for num in range(1, n2):
            #if num % n1 == 0:
            #print(num)
 
 #if n2 is positive do range(1, n2+1)
 #if n2 is negative do range(1, n2-1, -1)
 
 
 
 #       for index in range(1, n2):
 #           if index % n1 == 0:
 #              print(index)
 #       if n2 % n1 == 0:
 #           print(abs(n2))

#Divide 1..n2 by n1 and return all whole numbers