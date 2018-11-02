# Lab 07: Modeling spring motion and spring energy

## C-level Group Questions

Group Names: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


### Part 1 of 2

Below shows a short excerpt of code (similar to one on pg. 74 in your text, in
Chapter 2, Section 7) to model a ball hanging from a vertical spring with stiffness $k_s$.

``` {.python .numberLines startFrom="10"}
# SEVERAL LINES OF CODE BEFORE THIS ARE OMITTED
while True:
    rate (100)
    F_grav = vector(0, -g * m_ball, 0)
    L = ball.pos - spring.pos
    Lhat = norm(L)
    s = mag(L) - L0
    F_spring = -ks * s * Lhat
    F_net = F_grav + F_spring
    p_ball = p_ball + F_net * deltat
    ball.vel = p_ball / m_ball
    ball.pos = ball.pos+ ball.vel * deltat
```

1. Does the code correctly calculate the spring force on the mass? Explain. \vspace{0.5in}
1. Which line is calculating the momentum update of the mass? Explain.  \vspace{0.5in}
1. Which line is calculating the position update of the mass? Explain.  \vspace{0.5in}
1. Why are the F\_grav and F\_spring calculated inside the while loop? Is
  it necessary to do so? Explain. \vspace{0.5in}
1. Briefly describe what code needs to be included before line \#10.

\eject

### Part 2 of 2

Go to the simulation from the pre-lab at https://phet.colorado.edu/sims/html/masses-and-springs/latest/masses-and-springs_en.html

Change these settings in the simulation:

+ Check the displacement/natural length box. It shows where the spring would rest if there was no mass hanging from it.
+ Check the mass equilibrium box. It shows where the mass hangs in equilibrium, the point where the gravitational force and the spring force are balanced.
+ Set the damping to something large. This will make the mass quickly settle to the equilibrium position.

1. How much is the spring stretched when it is in equilibrium with the mass hanging on it? Your answer should be a *formula*. Use the variables $L_0$ for the unstretched length of the spring, $L$ for the length in equilibrium, $m$ for the mass of the block and $k_s$ for the stiffness of the spring. \vspace{2in}
2. What is the position of the ball when it is in equilibrium? Your answer should be a three-component vector.
