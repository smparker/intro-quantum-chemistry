# How To: Set Up Turbomole Using Define

When using Turbomole from the command line, the interactive program
`define` is used to prepare calculations. Essentially, all of the inputs
needed for a calculation are figured out during the `define` stage and
then separate programs are used to run the actual calculations. The
inputs for the calculation will include

-   the molecular coordinates (converted to the right form from an xyz
    file)
-   the computational model (method, etc.)
-   the computational parameters (basis set, convergence, etc.)

## Video

This video (17 minutes) walks you through your first time running
define. I recommend following along on your own terminal as you watch
this so you can compare your outputs to the ones shown on the video.

:::{youtube} gpVGdUDTAY8
:::

## Quick reference

For convenience, here is a really brief summary of the contents of the
video, for when you just want some quick answers.

### Load turbomole 

Before running any Turbomole commands, you must first set up your
environment by running

    module load turbomole/serial

in your terminal. If this command gives you an error, you may need to
run

    module use /home/smp201/.usr/local/share/modulefiles

and then try again. You can verify it was loaded correctly by running
the command

    sysname

which should output

    em64t-unknown-linux-gnu

### Prepare coord file

Make sure an appropriate `xyz` file is in your directory and then run

    x2t molecule.xyz > coord

### Define: first steps

Start define by running

    define

-   Always press \<enter\> at the first prompt
-   At the second prompt, (optionally) enter a title

### Geometry menu

-   `a coord` to load your coord file
-   `desy` to automatically determine symmetry
-   `ired` to determine internal coordinates
-   `*` to move on

### Basis menu

-   `b all def2-SVP` to set the def2-SVP basis for all atoms
-   `*` to move on

### Initial wavefunction menu

-   `eht` to use extended Hückel theory guess
-   `<enter>` to use default parameters
-   `0` to specify neutral molecule
-   `<enter>` to accept default occupation

### Method menu

#### DFT

-   `dft`
-   `on`
-   `func tpss` to set the TPSS functional
-   `<enter>`

#### Resolution of the Identity (RI)

-   `ri`
-   `on`
-   `<enter>`

MARIJ

-   `marij`
-   `<enter>`

Dispersion corrections

-   `dsp`
-   `bj`
-   `<enter>`

#### Exit

-   `*`
