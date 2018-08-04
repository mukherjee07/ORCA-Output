# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:20:26 2018

@author: Krish
"""

""" 
Objective : to Generate random coordinates of 24 Li atoms attached on NTCDA Surface
Input : Null
Outut : Coordinates which have been seperated at least 2/3rd of Li-Li distance

"""
"""import random
import math
# making matrix for storing X,Y,Z coordinates
X = [0 for y in range(24)]
Y = [0 for y in range(24)]
Z = [0 for y in range(24)]
temp_x = 0
temp_y = 0
temp_z = 0
c=0
x=0
trial = 0
 # Counter 
Dilithium = 2.2 # Li-Li Bond distance
while x<24 and trial < 500000:
  trial +=1
  print x
  Length = 0
  count = 0
  temp_x = random.uniform(-5,5)
  temp_y = random.uniform(-3,3)
  temp_z = random.uniform(-1,1)
  for y in range(x):
      # Making sure that the randomly generated coordinates are faraway from previous coordinates
      Length = math.sqrt((temp_x-X[y])**2.0 + (temp_y-Y[y])**2.0 + (temp_z-Z[y])**2.0)
      if Length > Dilithium:
          count = count + 1
      
          
  if count == x:
       X[x] = temp_x
       Y[x] = temp_y
       Z[x] = temp_z
       c += 1
       x += 1
 
      
#print c 
print X
print Y
print Z"""
import random
print random.randint(1,24)

      
         
  