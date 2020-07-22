#!/usr/bin/env python
import sys

fileostuff = sys.argv[1]

#Parse a file and count instances for each group of '10s (0-9, 10-19, 20-29,...) up to the max group from the input. 
#You should account for every group of 10 available in range from 0 to the max group of 10's from the input.
#Output is not binary...

#each digit represents a count of the number of times a number in a list falls in that list

with open (fileostuff, 'r') as stuff:
    numlist = []
    for line in stuff:
        numlist.append(line.strip())
    while '' in numlist:
        numlist.remove('')
    index = 0
    tens = 10
    limit = 10
    #find highest tens value and set that as limit
    #for item in list if item < tens then figure out what tens value is and set limit to that
    for number in numlist:
        if int(number) < tens:
            print("Got one!")
            index = index+1
    print(index)


    #in range set, set+10 and index++ for item in list that matches criteria
    #add 10 to set and do again until....
    #find highest 10s value and stop after set == highest_value