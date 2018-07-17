from __future__ import division, print_function
from visual import *

# Here are some lines to set up the scene
# Make the ground, an ignition box, and the rocket

scene.background=(0.5,0.55,0.7)
origin=vector(0,0,0)
box_origin=origin-vector(2,-0.5,0)
rocket=frame()
ground=box(pos=origin, size=(15,0.8,15), color=(0.30, 0.30,0.2))
ignition=box(pos=box_origin, size=(1,1,1), color=color.cyan)
body_axis=vector(0,2,0)
body=cylinder(frame=rocket, pos=origin, radius=0.1, axis=body_axis, color=color.red)
nose=cone(frame=rocket, pos=body.pos+body_axis,radius=0.1, axis=body_axis/5, color=color.green)


# Initialize constants in the situation
# The initial momentum, velocity of the rocket.
# Also define the force of gravity

mass=0.150
rocket.velocity=(0,10,0)
rocket.momentum=moss*rocket.velocity
Fgrav=mass*vector(0,-3.0,0)

# Initialize time and the time step
time=0.0
delta_time=0.1
wait_time=1/delta_time

# Animate time

while time < 3.0:
    Fnet=Fgrav
    #Include a statement here for the momentum principle to update the rocket.momentum
    # Realize that this is a vector, not just a single component!
    
    
    #Include a statement here to update the rocket.pos
    # Realize this is a vector and not a single component!
    
    scene.center=rocket.pos
    
    # When you have the rocket going,  make sure to show graphs in time of
    # rocket.momentum and rocket.pos
    
    time=time+delta_time
    rate(wait_time)

    # Need to debug?  Always good to print things out!
    
    
