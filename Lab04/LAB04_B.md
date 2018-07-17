**LAB 4: Modeling Non-constant Forces**

**Objectives:**

-   Learn how to model a force that depends on time

-   Learn how to model a force that depends on velocity

-   Use sum of forces acting on a system to model its motion

**Statement of the problem:** You are creating a simulation program in
VPython that will help you determine the flight characteristics of a
model rocket prior to building and launching the rocket. You would like
to include in the simulation gravity, thrust of the rocket motor, and
air drag.

**THE DRAG EQUATION FOR DRAG FORCE: **

$$[\overrightarrow{\mathbf{F}_{\mathbf{D}}}\mathbf{= -}\frac{\mathbf{\text{CAρ}}}{\mathbf{2}}\left| \overrightarrow{\mathbf{v}} \right|^{\mathbf{2}}\widehat{\mathbf{v}}]$$

**EQ. 1**

where C is a dimensionless number called the "coefficient of drag", A is
the cross-sectional area of the object in flight, ρ is the density of
the fluid (here air) through which the object moves and **v** is the
velocity vector of the object. You think this equation is pretty
straightforward, except you cannot seem to find a single value for the C
coefficient. Most sources say this coefficient is close to 1, but
depends on the shape of the flying object.

**THE THRUST CURVE FOR THE ROCKET ENGINE IS INCLUUDED IN THE LAB 4
MODULE AS A SEPARATE DOCUMENT ON D2L.**

**B-level**

-   VPython code called "rocket2.py" is available for you to start from.
    This code has the F\_engine of the rocket motor built in, but has
    some bugs and some missing pieces. First, debug the program.

-   You will need to implement a number of things in the code to get it
    to model your rocket. It is probably easiest to implement gravity
    and the engine thrust forces first. (NOTE: the F\_engine is coded as
    a list. Do not change the time in the burn loop or the list cannot
    work!) Make sure these make the rocket behave properly.

-   Air drag may be the most difficult force to implement in the code.
    Talk through with the instructor, a lab TA, or a group nearby to
    make sure you understand the equation in EQ. 1 before trying to code
    it in.

-   Once air drag is implemented in VPython, be sure to plot the
    momentum.y and position.y of the rocket in its flight. Lines to plot
    these are included in the code---you merely need to uncomment them.

-   Determine the flight time of the rocket and make sure it is
    reasonable. Note that you will be comparing real rocket flight data
    to what the code predicts in the next lab!

**TO TURN IN:**

-   A Word document including all participants' names.

-   A link to your Public working rocket program.

-   Screen shots showing the momentum and position of the rocket in
    time.

-   Indicate on your momentum graph the time when the burn loop stopped
    (engine ran out of fuel).

-   Include statements that indicate *how you know* your code is working
    properly.
