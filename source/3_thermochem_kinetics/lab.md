# Lab: Selectivity of Diels-Alder Reactions

## Introduction

In this lab, you will use density functional theory calculations to
predict the regioselectivity of the Diels-Alder reaction between
1-methyl 1,3-butadiene and propenoic acid (acrylic acid) to produce
a disubstituted cyclohexene. This reaction
can produce two unique products with either "ortho" or "meta" substitution
of the cyclohexene.{cite}`Kahn1986JACS`

:::{figure} /_static/diels-alder-reactions.png
:alt: Diels-Alder product with "ortho" and with "meta" substituted products.

Comparison of Diels-Alder reactions that produce "ortho" and "meta"
substitued cyclohexene.
:::

You will use density functional theory (DFT) calculations to predict which disubstituted product
is preferred and what the degree of selectivity is.
The free energy for each structure should be computed as

$$
G = E_{\text{elec}} + E_\text{ZPE} + G_\text{RRHO}
$$

where

- {math}`E_{\text{elec}}` is the electronic energy
- $E_\text{ZPE}$ is the zero-point energy
- $G_\text{RRHO}$ is the free energy correction from the rigid-rotor harmonic oscillator model

To get the most bang for our computational buck, a common approach is to use
a mixed methodology in which you use a "cheap" method to
compute structures, zero-point energy and free energy corrections, and then
a "more accurate" method to compute the electronic energy. The reasoning for this
is that the vibrational degrees of freedom (structure, ZPE, RRHO) tend to be
less sensitive to the method details than the electronic energy is.
In this lab, you will use a smaller basis set (def2-SVP) for the structure,
ZPE, and RRHO corrections and a larger basis set (def2-TZVP) for the electronic energy.
Reminder, pay attention to units!

As a measure of the
selectivity, use the ratio between concentrations between the two products,
$$ s = \frac{[\text{ortho}]}{[\text{meta}]}. $$
The free energy for a reaction is
$$ \Delta G = \sum_{p\in\text{products}} G_p - \sum_{r\in\text{reactants}} G_r. $$
For a kinetically controlled reaction, the ratio of the concentrations will
be determined by the ratio of the rates,

$$ s = k_1 / k_2. $$
According to transition state theory, the rate of a reaction is
$$ k = A e^{-\Delta G^\dagger/k_BT} $$
where $\Delta G^\dagger$ is the free energy difference between the
reactant complex and the transition structure, $k_B$ is the Boltzmann constant
and $T$ is the temperature. The factor $A$ is an extremely complicated factor
that accounts for how frequently the reactants come into close enough contact
with each other to possibly react. We typically can not estimate $A$ effectively,
but it is reasonable to expect that for two similar reactions (like we are looking
at here), the $A$ will be nearly the same. Thus we can remove the effect of $A$
by computing **relative rates**. Suppose you have two similar reactions
with rates $k_1$ and $k_2$ and free energies $\Delta G_1^\dagger$ and $\Delta G_2^\dagger$.
The relative rate would then be

$$ s = \frac{k_1}{k_2} = \frac{A \exp(-\Delta G_1^\dagger/k_BT)}{A \exp(-\Delta G_2^\dagger/k_BT)} = e^{(\Delta G_2^\dagger - \Delta G_1^\dagger)/k_BT} $$

For a thermodynamically controlled reaction, the ratio will be determined by
the ratio of the equilibrium constants, $K_1/K_2$, where
$$ K_1 = e^{-\Delta G_1/k_BT}. $$
Thus,
$$ s = K_1/K_2 = e^{(\Delta G_2 - \Delta G_1)/k_BT}. $$

### Prelab questions

1. Speculate which product you think will be thermodynamically favored. Why?
2. Speculate which product you think will be kinetically favored. Why?

## Procedure

Use thermochemistry analysis and transition state theory to predict the
reaction energies and the reaction rates for the two reactions discussed in the
introduction. Use the TPSS/def2-SVP/D3(BJ) functional and basis set for all
geometry optimizations and vibrational structure calculations followed by
TPSS/def2-TZVP/D3(BJ)/COSMO single point calculations for the electronic energy.
Assume room temperature for all free energy corrections.
To break it down more specifically, this means that for each structure you
need to compute, you should

1. Optimize the geometry using TPSS/def2-SVP/D3(BJ)
2. Compute vibrational spectra using TPSS/def2-SVP/D3(BJ)
  1. Verify that there is the right number of imaginary vibrational modes
  2. Use the vibrational structure data to compute the free energy corrections
3. Compute a single point energy (no geometry optimization!) using TPSS/def2-TZVP/D3(BJ)/COSMO

In total, you need to find 8 structures:

1. Isolated reactants (butadiene and acrylic acid)
2. Reactant complex ("ortho" and "meta")
3. Transition structure ("ortho" and "meta")
4. Isolated products ("ortho" and "meta")

## Discussion

In your discussion, answer the following questions

1. Which product would be favored thermodynamically? What would the expected ratio of the
  two products be if they were in equilibrium?
2. Which product would be favored kinetically? What would the expected ratio of
  the two products be if they were fully kinetically controlled?
3. Experimentally, the regioselectivity is 7.3:1 (ortho:meta). How does this
  compare to your computed results?
4. Suppose you wanted to test a large number of potential dienophiles
  for the resulting regioselectivity. How could you streamline your
  process to try and compute many transition states with less effort?
