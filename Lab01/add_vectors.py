from __future__ import division, print_function
from visual import *

# Comment names in for your group
# Start a new code with variables and initialized objects

# Two vectors A and B
# are defined using magnitude and direction (CCW degrees from x axis)
# Origin is also a useful definition

#Convert angles from degrees to radians
pi=3.141569265
deg2rad=pi/180
magA=100
dirA=45*deg2rad
magB=170
dirB=210*deg2rad
# Figure unit vectors from direction cosines
unitA=vector(cos(dirA),cos(dirA-pi/2.0),0)
unitB=vector(cos(dirB), cos(dirB-pi/2.0),0)

# Final vector determination.
# Defining the origin is also useful.
origin=vector(0,0,0)
A=magA*unitA
B=magB*unitB

# Create arrows for the two vectors
# Use tip to tail graphical representation
# That is, arrowB needs to start at the tip of arrowA

arrowA=arrow(pos=origin, axis=A, color=(1,0,0))
arrowB=arrow(pos=arrowA.axis, axis=B. color=(0,1,0))

# Math, figure the sum of the two vectors
# Then flip it to get the counterbalance.
V_sum=A+B
V_balance=-V_sum
print(V_balance)

#Check that the balance vector is OK in the Python Shell
# Now create a blue arrow that represents the opposite of A+B
# It starts at the tip of B and goes back to origin

