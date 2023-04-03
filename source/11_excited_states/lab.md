# Lab: UV-Vis spectroscopy

So far, this course has been concerned with properties of the electronic ground
state. When molecules are electronically excited, their physical and chemical
properties often change dramatically. Molecules often can be electronically
excited by electromagnetic radiation in the visible (VIS) or ultraviolet (UV)
spectrum{cite}`klessinger1995excited`. According to the Franck-Condon principle, electronic excitations
are vertical, i.e., there is no nuclear relaxation during an electronic
transition. In the simplest case, the absorption maximum in a UV-VIS spectrum is
located at the vertical transition energy,

$$E_n(X) − E_0(X) = hc/\lambda$$

where $X$
denotes the nuclear coordinates of the electronic ground state minimum, $h$ is
Planck’s constant, $c$ the speed of light, and $\lambda$ the absorption wavelength.

In this lab, you will use TDDFT to simulate the UV-vis absorption spectra
for two dyes commonly found in commercial sunscreens. From your simulated
results, you will then be able to assign orbital mechanisms to the particular
excitations.

## Selection Rules

Within the dipole approximation, the transition probability for an electronic
excitation from the ground to the $n$th excited electronic state is proportional
to the square of the electric transition dipole moment,

$$\mu_{0n}=-\int d\tau\Psi_0^* \mathbf{r} \Psi_n.$$

$\mu_{0n}$ is non-zero if the direct product of the electronic ground and the
excited state irreducible representations of the molecular point group contain
the dipole representation. The frequency integral of an absorption band is
proportional to the oscillator strength

$$f_{0n}\frac{2}{3}(E_n−E_0)|\mu_{0n}|^2$$

Time-Dependent Response Theory Molecular UV-VIS spectra can be efficiently
computed using time-dependent response theory{cite}`Furche2005CP`. The conceptual idea is to
apply a monochromatic external perturbation (e.g. a laser field) of
frequency $\omega$, and to consider the time-dependent response of a
molecular property such as the dipole moment. When the frequency $\omega$ equals an
electronic excitation energy of a dipole-allowed transition, the linear
response diverges. This is called the resonance catastrophe and it is the
conceptual route by which excitation energies are defined in TDDFT.

## Problems
In this lab, you will study the UV-vis spectra of

  - oxybenzone, a benzophenone derivative with IUPAC name (2-Hydroxy-4-methoxyphenyl)-
phenylmethanone
  - 2-ethylhexyl p-methoxycinnamate

:::{figure} /_static/uvvis-oxybenzone-cinnamate.jpg
:alt: Oxybenzone and 2-ethylhexyl p-methoxycinnamate (cinnamate)

Oxybenzone and 2-ethylhexyl p-methoxycinnamate (cinnamate)
:::

The experimental UV-vis spectra are shown below.{cite}`Walters1997JCE` The oxybenzone spectrum
has peaks at 326 nm and 288 nm, while p-methoxycinnamate has a peak at 310 nm.

:::{figure} /_static/uvvis-oxybenzone-cinnamate-abs.jpg
:alt: UV-Vis absorption spectra of oxybenzone and cinnamate

UV-Vis absorption spectra of oxybenzone and cinnamate
:::

1. Optimize the structure of each molecule using TPSS-D3(BJ)/def2-SVP/RI
2. Perform a vertical excitation energy calculation using PBE0-D3(BJ)/SVP.
Include 5 excited states.
3. Assign all 3 peaks in the experimental absorption spectra (2 peaks in
  the oxybenzone spectrum, 1 in the p-methoxycinnamate spectrum). Present
  all of the results in a table.
  1. Determine which excited state(s) is/are mainly responsible for the
  band.
  2. Extract the single-orbital transitions for each important excitation.
  In other words, find the most important occupied to virtual transition
  and organize it as, for example, HOMO->LUMO or HOMO-1->LUMO. Also collect
  the percentage of the transition described by the given transition.
  3. Visualize the MOs in TmoleX and describe the transitions with reference
  to these orbitals. Do they involve $\pi$ orbitals? Lone pairs? $\sigma$ bonds?
4. The most harmful portion of the UV to human skin is UVB, which covers
  290-315 nm. Which sunscreen offers more protection in the UVB? What about at
  350 nm?

