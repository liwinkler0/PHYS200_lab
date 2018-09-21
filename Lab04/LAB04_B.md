# LAB 4 Realistic model of a rocket motion
## B level: Modeling Non-constant Forces

### Objectives
-   Learn how to model a force that depends on time
-   Learn how to model a force that depends on velocity
-   Use sum of forces acting on a system to model its motion

**Statement of the problem:** You are creating a simulation program in
VPython/Glowscript that will help you determine the flight
characteristics of a model rocket prior to building and launching the
rocket. You would like to include in the simulation gravity, thrust of
the rocket motor, and air drag.

**Equation for drag force**

$${\overrightarrow{F}}_{D} = - \frac{\text{CA}\rho}{2}\left| \overrightarrow{v} \right|^{2}\widehat{v}$$

where C is a dimensionless number called the "coefficient of drag", A is
the cross-sectional area of the object in flight, $\rho$ is the density of
the fluid (here air) through which the object moves and $\vec{v}$ is the
velocity vector of the object. You think this equation is pretty
straightforward, except you cannot seem to find a single value for the C
coefficient. Most sources say this coefficient is close to 1, but
depends on the shape of the flying object.

There are two very useful functions in vpython that will help in
calculating the drag force:

-   `mag(my_vector)` calculates the magnitude of the vector `my_vector`,
    and

-   `norm(my_vector)` calculates the unit vector in the direction of `my_vector`.

**THE THRUST CURVE FOR THE ROCKET ENGINE IS INCLUUDED IN THE LAB 4
MODULE AS A SEPARATE DOCUMENT ON D2L.**

**B-level**

-   VPython code called "lab04rocket.py" is available for you to start
    from. This code has the F\_engine of the rocket motor built in, but
    has some bugs and some missing pieces. First, debug the program so
    that it runs.
-   Next, make sure all of the forces except air drag are included
    properly (do *not* start on air resistance yet). Use the position
    and momentum graphs of the rocket's motion to explain how you know
    the code is working correctly. You should use the information you have
    from Lab 03, in which you spent time thinking about this specific
    case.
-   Air drag may be the most difficult force to implement in the code.
    Talk through with the instructor, a lab learning assistant, or a
    group nearby to make sure you understand the equation in EQ. 1
    before trying to code it in.
-   Add air drag to the code. Make sure the code output seems
    reasonable by checking a limiting case. One way to do that is to change one or more of the
    parameters (like *C*) that go into the air drag and see whether the
    graphs of position and momentum change in the way you would expect.
-   Determine the flight time of the rocket and make sure it is
    reasonable.
-   Make the drag coefficient or area large enough that the rocket clearly
    reaches terminal velocity. Compare the terminal velocity from your code
    with the formula you came up with in the last part of the C level.
-   Draw a design (it can be a simple sketch) for the rocket you will build. You
    will be given a tube and a nos cone; you mainly need to decide how many
    fins to put on the rocket and what shape to make them.
-   Note that you will be comparing real rocket flight data to what the
    code predicts in the next lab!

**What to include in your write-up:**

-   Names of the people you worked with and what role they played.
-   A public link to your glowscript code.
-   Explain how you know the code was working before you added air
    resistance. That explanation should include a screen shot of you
    whatever graphs you use to explain/justify your answer (and your
    answer should refer in some quantitative way to at least one graph).
-   Explain how you implemented air resistance and how you checked
    whether your implementation was correct. Include in your explanation
    one or more graphs of the motion with air resistance and describe
    how the graph(s) support your conclusion that you did air drag
    correctly.
-   Report the time of flight you obtained for the rocket.
-   Include a drawing of your design for the rocket you will build.
