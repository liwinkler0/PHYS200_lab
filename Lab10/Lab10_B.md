# Lab 10: Rotational motion

## B-level experiments

### Objectives

-   Explore rotational motion
-   Compare periodic motion of a pendulum to a mass on a spring
-   Compare theoretical period to simulated and observed period

## Part 1: Simulation

1. Run the pendulum simulation in glowscript/vpython. Answer these questions:
    1. Start the pendulum at $\theta = 3.13$ (almost vertically upside down).
        + Is the motion of the pendulum periodic, i.e. does it repeat? Explain.
        + Imagine graphing $\theta$ as a function of time. Is the graph sinusoidal (i.e. a sine or cosine wave)? Explain.
    2. Start the pendulum at $\theta=0.1$ (close to vertical).
        + Is the motion of the pendulum periodic, i.e. does it repeat? Explain.
        + Imagine graphing $\theta$ as a function of time. Is the graph sinusoidal (i.e. a sine or cosine wave)? Explain.
2. Uncomment the lines in the simulation that display the angle $\theta$ and the angular velocity $\omega$. Answer these questions:
    1. Start the pendulum at $\theta = 3.13$ (almost vertically upside down).
        + Is the graph of $\theta$ sinusoidal (i.e. a sine or cosine wave)? Explain
        + Is the graph of $\omega$ sinusoidal? Explain
        + Include a screenshot of this graph in your writeup, labeled $\theta = 3.13$.
    2. Start the pendulum at $\theta=0.1$ (close to vertical).
        + Is the graph of $\theta$ sinusoidal (i.e. a sine or cosine wave)? Explain
        + Is the graph of $\omega$ sinusoidal? Explain
        + Include a screenshot of this graph in your writeup, labeled $\theta=0.1$.
3. For the small starting angle, compare the largest value of $\omega$ to the value from your formula in the C level.

## Part 2: Experiment

1. Attached a mass to the end of one of the rods for the rotary motion sensor. Make sure you measure its mass first.
2. Attach the rod to the rotary motion sensor.
3. Zero the rotary motion sensor with the rod hanging straight down.
4. Pull the rod to the side a little bit, start collecting data, and release the rod.
5. Fit a sine curve to either the angle as a function of time or the angular velocity. *Include a copy of this graph in your write-up.*
6. Calculate the period of the motion from the fit parameters like you did in Lab 7. *Include the period you measure in your write-up.*
7. It turns out that there is a formula for the period if the starting angle is small. The formula is $T = 2\pi \sqrt{\ell/g}$, where $\ell$ is the distance from the pivot point to the mass.
    + Measure $\ell$ for your setup and compute the period.
    + Compare the period you computed to the one you measured from the experiment.

## Part 3: Compare simulation, experiment and experiment

1. Set the parameters in your program to match the ones in your experiment.
2. Measure the period in the simulation (e.g. from the graph or by printing something appropriate from the progam).
3. Compare that period to the one from the experiment and from the formula.
