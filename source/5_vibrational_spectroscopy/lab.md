# Lab: Vibrational Spectroscopy

## Introduction

In this lab, we will investigate the structure and infrared vibrational
spectrum of hydrated hydronium ions in the gas phase, $\ce{H3O+.(H2O)_n}$
for $n$=1,2,3. Hydrated hydronium ions are the most fundamental models one
can make about acids in solution and are also important species in the
ionosphere.{cite}`Yeh1989JCP`

Starting with the simplest hydrated hydronium cluster possible,
$\ce{H5O2+}$, there are already interesting fundamental questions. For
instance, is the most stable structure of $\ce{H5O2^+}$ one in which a
hydronium atom is complexed with a water molecule, $\ce{H3O+ . H2O}$,
or one in which a proton is shared between two water molecules,
$\ce{H2O.H^+.OH2}$?
This question essentially boils down to, does it make sense to think of
the hydronium ion as a species?

### Prelab questions

-   What structure would you expect the hydronium ion to have? With what
    molecule is it isoelectronic?
-   Speculate how could you distinguish between the two structures? What
    geometrical parameter(s) would indicate one versus the other?

## Lab

Predict the structure and vibrational IR spectrum of the following
species

-   $\ce{H2O}$
-   $\ce{H3O+}$
-   $\ce{H3O+ . (H2O)_n}$ for $n$=1,2,3

### Procedure and Discussion Questions

1.  For each molecule (5 in total), optimize geometries using
    TPSS-D3(BJ)/def2-SVP/RI. For the hydrated hydronium clusters, be
    sure to use your chemical intuition while building structures and
    then use simulated annealing to find good initial guesses. For the
    simulated annealing, use the xtb method with initial temperature
    1000K, time step 40 a.u., annealing rate 0.95, and run a total time
    of 80000 a.u., with annealing starting after 20000 a.u.
2.  Compute vibrational frequencies for each molecule above.
3.  Find the vibrational frequencies for all stretching modes for water
    and hydronium. Classify the modes as either a \"symmetric stretch\"
    or an \"asymmetric stretch\" by visualizing them. **Organize the**
    **results into a table. What effect does the proton have on the**
    **vibrational frequencies?**
4.  For each of the hydrated hydronium structures, find all vibrational
    modes that correspond to stretches. Classify the modes as symmetric
    or asymmetric. By visualizing and comparing their frequencies with
    the stretch frequencies for water and hydronium, further classify
    the modes as belonging to $\ce{H2O}$ or $\ce{H3O+}. **Organize all of the**
    **results in a table. Report vibrational frequencies in wavenumber**
    **(cm^-1^).**
5.  Using your computed results, assign vibrational modes to each of the
    labeled features in the experimentally measured spectra below.
    **Organize the results in a table.**
6.  Compare the measured spectra to the computed vibrational
    frequencies. Using the optimal scaling parameter given in the table
    in the lecture, compare the measured spectra to computed and scaled
    vibrational frequencies. **Estimate errors in the stretch frequencies**
    **for both the unscaled and the scaled frequencies. This should be a**
    **numerical estimate with a unit.** 

::::{subfigure} ABC
:name: hydronium vibrational spectra
:gap: 8px
:layout-sm: A|B|C

:::{image} /_static/hydronium_vib_n1.png
:alt: n=1
:::

:::{image} /_static/hydronium_vib_n2.png
:alt: n=2
:::

:::{image} /_static/hydronium_vib_n3.png
:alt: n=3
:::

Spectra of hydronium ions with $n$=1,2,3
::::

**Does the hydronium exist in solution? Argue using your results and the**
**experimental spectra.**
