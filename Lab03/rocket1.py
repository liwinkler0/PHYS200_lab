from vpython import *
# Zone 1: This is complete!
# Here are some lines to set up the scene
# Make the ground, an ignition box, and the rocket (a compound object)

scene.background = (0.5, 0.55, 0.7)
origin = vector(0, 0, 0)
box_origin = origin - vector(2, -0.5, 0)

ground = box(pos=origin,
             size=vector(15, 0.8, 15),
             color=vector(0.30, 0.30, 0.2))

ignition = box(pos=box_origin,
               size=vector(1, 1, 1),
               color=color.cyan)

body_axis = vector(0, 2, 0)
body = cylinder(pos=origin,
                radius=0.1,
                axis=body_axis,
                color=color.red)

nose = cone(pos=body.pos + body_axis,
            radius=0.1,
            axis=body_axis / 5,
            color=color.green)
rocket = compound([nose, body])

# These statements will be needed to set up momentum and position graphs.
graph_pos = gdisplay(title='position', xtitle='time', ytitle='y')
pos_curve = gcurve(color=color.cyan)
graph_mom = gdisplay(title='momentum', xtitle='time', ytitle='py')
mom_curve = gcurve(color=color.green)

# Zone 2: This is complete! But there are some silly errors...
# Initialize constants in the situation
# The initial momentum, velocity of the rocket.
# Also define the force of gravity

rocket.mass = 0.150
rocket.velocity = vector(0, 10, 0)
rocket.momentum = rocket.moss * rocket.velocity
Fgrav = rocket.mass * vector(0, -3.0, 0)

# Initialize time and the time step
time = 0.0
delta_time = 0.1
wait_time = 1 / delta_time

# Zone 3: This is MISSING both momentum and position update statements!
# Animate time

while time < 6.0:
    Fnet = Fgrav
    # Include a statement here for the momentum principle to update the rocket.momentum
    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    # UPDATE MOMENTUM HERE

    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    # CALCULATE VELOCITY HERE

    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    # UPDATE POSITION HERE


    # Include a statement here to update the rocket.pos
    # Realize this is a vector and not a single component!

    scene.center = rocket.pos

    # These will plot your rocket.momentum and rocket.pos.
    # Leave them as comments until your motion is working!
    # ↓↓↓↓↓ REMOVE COMMENT HASHTAGS  FROM LINE BELOW AFTER YOU HAVE ROCKET MOVING   ↓↓↓↓↓
    # mom_curve.plot(pos=(time,rocket.momentum.y))
    # pos_curve.plot(pos=(time,rocket.pos.y))

    time = time + delta_time
    rate(wait_time)

    # Need to debug?  Always good to print things out!
