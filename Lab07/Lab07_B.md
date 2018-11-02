# Lab 07: Modeling spring motion and spring energy

## B-level experiment

### Objectives

-   Learn how to model a mass on a spring in 1-D
-   Investigate energy conservation in a spring-mass system
-   Develop more VPython skills in writing functions and graphing
    them

### Part 1: Spring Model

-   A minimal spring program is available on D2L. It integrates the
    motion but does not include the spring force.
-   Use the minimal code, the code from the C-level, and the following
    equation for the force exerted by a stretched spring, to develop a
    program that correctly models the mass on the spring.

    $$\overrightarrow{\mathbf{F}} = \  - k_{s}\text{s\ }\widehat{\mathbf{L}}$$

-   $\overrightarrow{\mathbf{L}}$ is the vector that points from the
    support point of the spring (considered to be $\langle 0,0,0\rangle$) to the mass
    supported on the end of the spring;
-   s=$\left| \overrightarrow{\mathbf{L}} \right|$ - $L_{0}$, with
    $L_{0}$ being the length of the spring with no mass attached.
-   Look at your setup from Lab 6 (mass on a spring) and change the mass
    of the block to match the mass you used and the spring constant to
    the spring constant you measured.
-   Change the starting position of the mass to the equilibrium position you
    calculated in the C-level.
    + If the block starts at rest at that position how should it move?
    + How does it actually move?
    + In your writeup include what the starting position was (both as a formula and a number) and describe what happened in your simulation.
-   You measured the period of your mass/spring system when displaced
    from equilibrium in Lab 6.
    + CHange the mass and spring stiffness to match the values from Lab 6. Be sure to use the value you measured for the spring stiffness, not the value the box said.
    + Measure the period of the mass in your simulation.
    + Compare the period from your simulation to the period you measured in Lab 6.
    + Your lab writeup should include the values you used for mass and stiffness as well as the values for the two periods you are comparing.

### Part 2: Spring Energy

You investigated potential energy, kinetic energy, and total energy in
the prelab. You will now modify the code to calculate and graph the
following inside the motion animation loop:

-   $U = U_{g} + U_{s}$ total potential energy of spring and gravity
-   $K$ kinetic energy of moving mass on spring
-   $E = K + U$ total energy
-   All three forms of energy may be placed in the same graphics window,
    using different colored curves to label them.

Formulas for each of these quantities are below:

-   $K=\frac{1}{2}\text{m\ }v^{2}$
-   $U_{g} = m\ g\ y$*,* where *y* is the y-component of the position of
    the block.
-   $U_{s} = \frac{1}{2}\text{k\ }s^{2}$, where $s$ is the spring
    stretch that appears in the spring force equation.

Questions to answer in this part of your lab write-up:

-   How many times per complete cycle is there a maximum in the kinetic
    energy? Compare that to the answer you gave in the pre-lab.
-   Describe the graph of the total energy and compare it to the
    behavior of the total energy in the pre-lab quiz.
-   Include a screenshot of your energy graphs.
