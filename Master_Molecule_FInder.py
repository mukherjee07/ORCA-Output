
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 23:36:46 2018
Objective : To find out nearest carbon and oxygen atom with respect to each Li atoms.
This will help us to understand the pathway which Li takes for binding to any structure.

Input : Optimised Geometry of ORCA output with xyz as the starting line before the geometry.

Suggestion : Copying the optimised Geometry using vi editor in a text file and 
putting that text file in the input is the best way.

@author: Krishnendu Mukherjee, MS Student, Chemical Engineering, University at Buffalo
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

# Code 2 Working
# Objective : To find the closest Carbon and Oxygen w.r.t to a Li atom

#Exporting Libraries
import math
import re   # Regular Expressions Library

#Getting the file and splitting the lines
file = open("CF3+19.txt")
lines = file.readlines() 
#finding the pattern = "*xyz"
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
# For findind positions of Li atoms       
c = 0 
w = 124  # approx 3 times of Li atoms. Better if you user input this.
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
                                
# For finding positions of Carbon atoms 
c1 = 0 
w1 = 60  # approx 3 times of Carbon atoms. Better if you user input this.
Carbon = [0 for x in range(w1)]   # 1-D Matrix to store Carbon atoms coordinates
k1 = 0  
for j in range(0,47):
    Port1 = re.split(r'/s',lines[s+j])
    for p1 in Port1:
        if re.search("C",p1):
            print "Carbon atom found"
            c1+=1 # No. of Li atoms
            for token1 in p1.split():
                
        # if this succeeds, you have your (first) float
                #while not re.search(">",token):
                if token1[0].isdigit() or token1[0]=='-' and not re.search(">",token1):
                        
                    
                            #Matrix[k][c] = float(token)
                            #k+=1
                    if not re.search(">",token1):
                                #print "float found",token
                            
                                Carbon[k1] = float(token1)

                                k1 = k1+1                        
if c1!=0:
    print "Number of Carbon atoms in your structure would be",c1 
    z = 0
else:
    print "You don't seem to have any Carbon atom in your structure !!!"
#print Matrix      
#Arranging the matrix file into proper xyz coordinates
    #Finding total of Li-Li Molecules
"""exp = 2.673 # Li-Li Bond length. You may keep it 5% more than Experimental value
for a in range(c):
    for b in range(a+1,c):
      Mol = math.sqrt((Matrix[3*a]-Matrix[3*b])**2.0 + (Matrix[(3*a)+1]-Matrix[(3*b)+1])**2.0 + (Matrix[(3*a)+2]-Matrix[(3*b)+2])**2.0)
      if Mol <= exp:
          print "There is an Li-Li bond formation happening at between",a+1,"position and",b+1,"Position"
          z +=1
          #print Mol
print z"""
      
#print Carbon
# For finding positions of Oxygen atoms 
c2 = 0 
w2 = 60  # approx 3 times of O atoms. Better if you user input this.
Oxygen = [0 for x in range(w2)]   # 1-D Matrix to store O atoms coordinates
k2 = 0  
for l in range(0,47):
    Port2 = re.split(r'/s',lines[s+l])
    for p2 in Port2:
        if re.search("O",p2):
            print "Oxygen atom found"
            c2+=1 # No. of Li atoms
            for token2 in p2.split():
                
        # if this succeeds, you have your (first) float
                #while not re.search(">",token):
                if token2[0].isdigit() or token2[0]=='-' and not re.search(">",token2):
                        
                    
                            #Matrix[k][c] = float(token)
                            #k+=1
                    if not re.search(">",token2):
                                #print "float found",token
                            
                                Oxygen[k2] = float(token2)

                                k2 = k2+1                        
if c2!=0:
    print "Number of Oxygen atoms in your structure would be",c2 
    z = 0
else:
    print "You don't seem to have any Oxygen atom in your structure !!!"

#print Oxygen

# For finding th nearest Oxygen to a certain Li atoms
# c no. of Li atoms, c2 No. of Oxygen atoms

for x in range(c):
    Least = 10
    Pos =0
    for y in range(c2):
         Moloxy = math.sqrt((Matrix[3*x]-Oxygen[3*y])**2.0 + (Matrix[(3*x)+1]-Oxygen[(3*y)+1])**2.0 + (Matrix[(3*x)+2]-Oxygen[(3*y)+2])**2.0)
         if Moloxy<Least:
             Least = Moloxy
             Pos = y+1
         else:
             continue
    print "For Li",x+1,"Closest Oxygen",Pos,"Distance",Least,"Angstorm"  
    
# For finding th nearest Carbon to a certain Li atoms
# c no. of Li atoms, c1 No. of Carbon atoms
for x in range(c):
    Least = 10
    Pos =0
    for y in range(c1):
         Molcar = math.sqrt((Matrix[3*x]-Carbon[3*y])**2.0 + (Matrix[(3*x)+1]-Carbon[(3*y)+1])**2.0 + (Matrix[(3*x)+2]-Carbon[(3*y)+2])**2.0)
         if Molcar<Least:
             Least = Molcar
             Pos = y+1
         else:
             continue
    print "For Li",x+1,"Closest Carbon",Pos,"Distance",Least,"Angstorm"  


    


