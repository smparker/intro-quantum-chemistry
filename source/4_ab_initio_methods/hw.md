# HW

## Introduction
In this lab we will, as a class, evaluate the performance of a handful
of first-principles methods on a benchmark database of reaction energies of Diels-Alder
reactions. In addition, we will examine the basis set convergence of
two representative methods.
The reaction database we will be using is known as
GMTKN55,{cite}`Goerigk2017PCCP` which stands for General Main-group Thermochemistry,
Kinetics, and Noncovalent interactions, and in particular, we will be
using the DARC subset which contains 14 reactions and requires 22
single-point calculations to evaluate.

### Basis set extrapolation

Basis set extrapolation is a
technique to estimate the complete basis set (CBS) limit. CBS
extrapolations are especially important for correlated methods (CC,
RIRPA, MP2, etc.). Results using CBS extrapolation are reported like
TPSS-D3/CBS(TZVP-QZVP)/RI, where the pseudo basis set CBS(TZVP-QZVP)
stands for a complete basis set extrapolation using calculations with
the TZVP and QZVP basis sets. It is also colloquially called a TQ
extrapolation. The formula used for the basis set extrapolation depends on
the type of method being used. There are generally two types of basis set
extrapolations commonly used: SCF extrapolations and correlated extrapolations.

### SCF extrapolation

Methods based on a self-consistent field (SCF) structure typically
converge exponentially with the basis set because the physical variable
in the calculation is the electronic density, which converges quickly.
SCF extrapolations should be used for

- Hartree-Fock (HF)
- Kohn-Sham Density Functional Theory (KS-DFT)

To extrapolate SCF type energies to the CBS, use the formula
$$ E_{\text{HF/DFT},\infty} = \frac{e^{B\sqrt{X}} E_{\text{HF/DFT},X} - e^{B\sqrt{Y}} E_{\text{HF/DFT},Y} } { e^{B\sqrt{X}}- e^{B\sqrt{Y}}} $$

where

- $E_{\text{HF/DFT},\infty}$ is the estimated energy at the CBS limit
- $E_{\text{HF/DFT},X}$ is the computed energy at a specific cardinality (e.g., the energy using
def2-TZVP is $E_{\text{HF/DFT},3}$.

Assume $B=6$ a.u. for HF and DFT extrapolations. Without this assumption, a third
calculation would normally be needed.

### Correlation energy extrapolation

Methods that directly compute the electron correlation from some sort of
wavefunction converge slow with the basis set.
Correlation energy extrapolations should be used for

- Moller-Plesset Perturbation Theory such as MP2, MP3, etc.
- Coupled cluster theory such as CCSD, CCSD(T)
- Random Phase Approximation (RI-RPA)

To extrapolate correlation energies use the formula
$$\Delta E_{\text{corr},\infty} = \frac{ X^n \Delta E_{\text{corr},X} - Y^n \Delta E_{\text{corr},Y} } { X^n - Y^n }$$
where

- $\Delta E_{\text{corr},\infty}$ is the estimated correlation energy at the CBS limit
- $\Delta E_{\text{corr},X}$ is the computed correlation energy at a specific cardinality (e.g., the
correlation energy from a cc-pVTZ calculation is $\Delta E_{\text{corr},3}$.

Use $n=3$.
It is crucial to remember that this formula applies only to the
correlation part of the energy, not the HF/DFT part of the energy. If
you also needed to extrapolate the HF/DFT part of the energy, you would
do a separate extrapolation of that. However, in practice, it is more
common to just do one calculation with a very large basis (e.g.,
def2-QZVP) for the HF/DFT part of the energy and not worry about the
extrapolation.

## Problems

Each group will compute single-point energies for 2-3 compounds
(depending on the size). All of the total energies will be submitted by
entering it into this [google
sheet](https://docs.google.com/spreadsheets/d/19ZhOnApWJX8hkrTWirDfafpnqsqeRLS_TRX6oUKV0UY/edit?usp=sharing).
These total energies must be submitted by Friday September 23, before the assignment is due.

The geometries for each molecule in the reaction set are helpfully
provided by the authors of Ref. {cite}`Goerigk2017PCCP` on their
[website](https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/GMTKN/gmtkn55).
The geometries have been placed on markov in the folder `~smp201/darc`
for easy use.

  ----------- ----------------- -------------------
   **Group**    **Molecule**     **geometry name**
       1           ethene           ethene.xyz
       1           ethine           ethine.xyz
       1          butadiene        butadiene.xyz
       2       cyclopentadiene      cpdiene.xyz
       2       cyclohexadiene       chdiene.xyz
       2           furane           furane.xyz
       3           malein           malein.xyz
       3          maleinNH         maleinnh.xyz
       3             P1               p1.xyz
       4             P2               p2.xyz
       4             P3               p3.xyz
       4             P4               p4.xyz
       5             P5               p5.xyz
       5             P6               p6.xyz
       5             P7               p7.xyz
       6             P7X              p7x.xyz
       6             P8               p8.xyz
       6             P8X              p8x.xyz
       7             P9               p9.xyz
       7             P9X              p9x.xyz
       8             P10              p10.xyz
       8             P10X             p10x.xyz
  ----------- ----------------- -------------------
  
  : Team Assignments

So for example, you can copy the structure for furane into your own
directory by running

```
cp ~smp201/darc/furane.xyz .
```

The reaction products are all labeled by P. For reactions 7, 8, 9, and
10 there are two products because the same reactants can produce two
different Diels-Alder products. The reactions are summarized by the
following figure:{cite}`Johnson2008JCP`

!image!

The reference reaction energies were originally computed using
complete basis set (CBS) CCSD(T) calculations and are

  ---- ---------- ----------- ------
  \#   dienophile diene       product              
  1    ethene     butadiene   P1
  2    ethine     butadiene   P2
  3    ethene     cpdiene     P3
  4    ethine     cpdiene     P4
  5    ethene     chdiene     P5
  6    ethine     chdiene     P6
  7    furane     malein      P7
  8    furane     malein      P7X
  9    furane     maleinNH    P8
  10   furane     maleinNH    P8X
  11   cpdiene    malein      P9
  12   cpdiene    malein      P9X
  13   cpdiene    maleinNH    P10
  14   cpdiene    maleinNH    P10X
  ---- ---------- ----------- ------
  
: Enumeration of reactions

### Calculations

Compute single-point on the molecules specified for your group using the
following method/basis combinations

1.  TPSS-D3(BJ)/def2-TZVP/RI
2.  TPSSh-D3(BJ)/def2-TZVP/RI
3.  TPSSh-D3(BJ)/def2-QZVP/RI
4.  RIRPA\@TPSS/def2-TZVP/RI
5.  RIRPA\@TPSS/def2-QZVP/RI
6.  RIMP2/def2-TZVP/RI

**Important:** do not optimize the geometries! We want to compare the
electronic energy at a specific geometry for all methods, so optimizing
the geometry will skew the results.

**Important:** when reporting calculation times for RIRPA and RIMP2, you
should include the calculation time of the DFT (RIRPA) and HF (RIMP2) step.
TmoleX does not show this by default, but you can find it by navigating
to the directory where the calculation was run and opening the `ridft.out`
file.

In addition, you will use the following methods for analysis, but the
data will be provided for you

1.  CCSD/def2-TZVP/RI
2.  CCSD/def2-QZVP/RI
3.  CCSD(T)/def2-TZVP/RI
4.  CCSD(T)/def2-QZVP/RI

## Problems

Use the results computed by your peers to complete the
following

1.  Use the data you have to perform TQ basis set extrapolations for TPSSh,
    RIRPA, CCSD, and CCSD(T).
2.  Compute the reaction energies for all 14 reactions using all 14
    methods (10 direct calculations plus 4 CBS extrapolated). This sounds like
    a lot but if you do it on a spreadsheet it is not. Report the reaction energies
    as a table in kcal/mol, including the reference energies.
3.  Compute the mean absolute error, the maximum error, and the
    root-mean-square-error across the whole test set for each of the
    methods described above. In addition, estimate the total amount of
    time to run the benchmark set by adding up the calculation times for
    all 22 compounds for each method. Collect the results in a table
    with units of kcal/mol for energy and minutes for time.
4.  Which method performed the best? The worst? Which method would you
    recommend to use if you only needed accuracy within 10 kcal/mol?
    Why? What about 5 kcal/mol? Why?
5.  Compare the basis set convergence of TPSSh and RIRPA using the TQ extrapolated
    energies as a reference value. Prepare a table with the mean absolute
    error for both methods relative to the TQ extrapolated result. What does
    this tell you about how quickly or slowly the two methods converge to the
    CBS limit?
6.  The reference results are essentially CCSD(T) in the infinite basis
    limit. With that in mind, evaluate the performance of
    CCSD(T)/def2-TZVP. Explain why it does or does not perform well.

