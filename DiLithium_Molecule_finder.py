
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 23:36:46 2018
Objective : to find out Li-Li bonding in the system and look for possible positions
@author: Krish
"""
#Code 1 Trial not working
"""print sys.version
#
#import string
#filename = "Orca.out"
#print file
#pattern = re.compile('*xyz')

#for i, line in enumerate(open('Orca.out')):
#   for match in re.finditer(pattern, line):
#      print 'Found on line %s: %s' % (i+1, match.groups())"""

# Code 2 hope it works
# Update : Its working :)
#import numpy as np
import math
import re   # Regular Expressions Library

file = open("OMe+12.txt")
lines = file.readlines() 
#pattern = "*xyz"
#print lines

for line in lines:
    part = re.split(r'/s', line)
    for p in part:
        if re.search("xyz",p):
          print "xyz coordinates found !!!"
          s = lines.index(line)
          print s 
          # s is the location from where we will get our coordinates
          break
    else:
        #Continue if the inner loop wasn't broken
        continue
    #Inner Loop was broken and hence break the outer Loop
    break   

#w = raw_input('How many atoms in your structure :')         
c = 0 
w = 124
Matrix = [0 for x in range(w)]   # 1-D Matrix to store Li atoms coordinates
k = 0  
for i in range(0,47):
    Port = re.split(r'/s',lines[s+i])
    for p in Port:
        if re.search("Li",p):
            print "Li atom found"
            c+=1 # No. of Li atoms
            for token in p.split():
                
        # if this succeeds, you have your (first) float
                #while not re.search(">",token):
                if token[0].isdigit() or token[0]=='-' and not re.search(">",token):
                        
                    
                            #Matrix[k][c] = float(token)
                            #k+=1
                    if not re.search(">",token):
                                #print "float found",token
                            
                                Matrix[k] = float(token)

                                k = k+1
print k                         
if c!=0:
    print "Number of Li atoms in your structure would be",c 
    z = 0
else:
    print "You don't seem to have any Li atom in your structure !!!"
#print Matrix      
#Arranging the matrix file into proper xyz coordinates
exp = 2.673 # Li-Li Bond length. You may keep it 5% more than Experimental value
for a in range(c):
    for b in range(a+1,c):
      Mol = math.sqrt((Matrix[3*a]-Matrix[3*b])**2.0 + (Matrix[(3*a)+1]-Matrix[(3*b)+1])**2.0 + (Matrix[(3*a)+2]-Matrix[(3*b)+2])**2.0)
      if Mol <= exp:
          print "There is an Li-Li bond formation happening at between",a+1,"position and",b+1,"Position"
          z +=1
          #print Mol
print z
      









