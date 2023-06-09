# Computing excited states with TDDFT

In this page, we will describe how to compute excitation energies
and absorption spectra using TDDFT through TmoleX. The turbomole manual
describes how to run absorption spectra calculations through the command line.

## Getting started

As always, be sure to `module load tmolex`. It is especially important to
always start from a good geometry. Excited state calculations are always
a bit more challenging than the ground state, so it's important to start with
a ground state calculation to make sure everything looks okay. If there
are problems with the ground state geometry or electronic structure (i.e., 
DFT geometry or orbitals) then the excited state calculations will fail
miserably. What counts as a "good geometry" will depend on the problem that
is trying to be solved, but the ground state geometry is always a reasonable
guess for a "good geometry".

Run a ground state single point energy and make sure that the electronic
structure converges and that when it converges, it has a HOMO/LUMO gap of
at least 1 eV or so. Anything less means TDDFT may not be appropriate.

## Specify the functional

For TDDFT calculations, hybrid functionals are really necessary to get
quality results. As an example here, we will select the PBE0 functional
for our excited-state calculations and an m4 grid.

## Setting up the excited state parameters

From the Start Job tab in TmoleX, choose "Spectra & Excited States" and
"UV/Vis and CD(vertical excitations)"

:::{image} /_static/uvvis.gif
:::

For absorption spectra, we want singlet excitations and we want to use the
flavor of TDDFT called the Random Phase Approximation (RPA). Select the "Singlet"
option for the excited state. Select "RPA- Random Phase Approx." from the
dropdown. Select a unit to display excitation energies (I recommend eV, but
it doesn't actually change any results, just what unit it's printed out in).
Finally, specify the number of excitations you want to find. This will be
determined by the problem.

:::{image} /_static/excited_state_settings.gif
:::

Once the excited state settings are chosen, you can run the calculation.

## Viewing the results
When it finishes, go to the results page and view the spectrum by
clicking on the "UV/Vis spectrum". The spectrum is generated by broadening
the individual excitations with a Gaussian or Lorentzian function. On the
spectrum page, you can see the individual transitions as vertical "sticks" and the
broadened spectrum as a line. You can also adjust the unit used to plot,
the width of the broadening.

:::{image} /_static/spectrum.gif
:::

For a more detailed view of each excitation, open the output file, and
scroll to a section that looks like


                             1 singlet a excitation


     Total energy:                           -575.4083620027358    

     Excitation energy:                      0.1351678889642150    

     Excitation energy / eV:                  3.678106976067825    

     Excitation energy / nm:                  337.0871070721735    

     Excitation energy / cm^(-1):             29665.92251291969    


     Oscillator strength:

        velocity representation:             0.5400985144816011E-03

        length representation:               0.1045298409128081E-02

        mixed representation:                0.7513745717687524E-03


     Rotatory strength:

        velocity representation:             0.2361353250144041E-03

        velocity rep. / 10^(-40)erg*cm^3:     15.25547931958575    

        length representation:               0.3284958514723984E-03

        length rep. / 10^(-40)erg*cm^3:       21.22241417458907    


     Dominant contributions:

          occ. orbital   energy / eV   virt. orbital     energy / eV   |coeff.|^2*100
           48 a              -7.13          49 a              -1.71       79.4
           45 a              -7.66          49 a              -1.71       15.6
     

     Change of electron number:

                -0.000000


     Electric transition dipole moment (velocity rep.):

        x       -0.008437        Norm:                  0.077419
        y       -0.054577
        z       -0.054257        Norm / debye:          0.196780


     Electric transition dipole moment (length rep.):

        x       -0.011660        Norm:                  0.107703
        y       -0.075960
        z       -0.075460        Norm / debye:          0.273757


     Magnetic transition dipole moment / i:

        x       -0.000392        Norm:                  0.003055
        y       -0.002033
        z       -0.002246        Norm / Bohr mag.:      0.837262


     Electric quadrupole transition moment:

       xx        1.341899
       yy       -0.448442        1/3*trace:             0.279563
       zz       -0.054768
       xy       -0.444400
       xz       -0.480155        Anisotropy:            2.012290
       yz       -0.191226

In this section, you can see all the detailed information about the
transition, including the energy in several units, the oscillator strength,
the orbitals involved in the transition, and some transition moments. Use the
listed energies to compare with the broadened spectrum and determine which
transitions are important.

## View orbitals

Finally, you may want to visualize the orbitals to see what transitions
are involved in greater detail. From the results page, open the
"Orbital/Density Plot". A 3D visualizer panel will show up that lets you
choose molecular orbitals to view, specialized densities, or
natural transition orbitals. For simplicity, in this case we're just going
to visualize the LUMO orbital. Click the check box to the left of the LUMO.
At the bottom of the window, click "Calculate selected" and then "View selected".
