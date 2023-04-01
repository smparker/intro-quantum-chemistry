# Types of Chemical Theories

There are three basic flavors of theories that we will discuss in this class
that organized by the origin of the theory.

## First principles

First principles theories, also known as "ab initio" theories (from the Latin for
"from the beginning") start from fundamental laws of physics and that's that.
For example, first principles theories are typically based either on the
Schrödinger equation (which governs all quantum behavior), the Dirac
equation (the extension of the Schrödinger equation to special relativity),
or statistical mechanics. Since none of these theories can be solved
exactly for any molecules that are all that interesting, the
practical methods we use for computation are schemes to approximate these
fundamental laws.

### Advantages
  - First principles methods are broadly applicable, because their only input
  tends to be universal physical parameters, like the number of protons and
  electrons in a molecule
  - Methods with a tight connection to the fundamental laws of physics hold
  the potential to become extremely accurate, often referred to as
  "spectroscopic accuracy" (although that's not to say
  that the high accuracy is computational affordable)
  - Because these methods are based on fundamental laws of physics and
  well-defined approximations to the related equations, method failures can
  often be rationalized (and hopefully fixed) fairly straightforwardly
  
### Disdvantages
  - First principles methods tend to be quite expensive, relative to the
  examples listed below
  
### Example: Density Functional Theory (DFT)
  - only required input is the positions of nuclei and the total number of
  electrons
  - calculations on hundreds of atoms is fairly routine
    
## Semiempirical models

Semiempirical models typically take first principles theories as motivation,
but then make large simplifications based purely on empirical evidence.
The result tends to be methods that have the same basic structure as
(some) first principles theories, but where fundamental laws were replaced with
parametrized interactions. For example, so called "tight binding" methods
(such as Hückel theory) ignore electron-electron repulsion and compensate for
it by introducing special parameters for the attraction between electrons and nuclei.
The empirical
evidence does not have to be experiment here. For example, semiempirical models
could be parameterized by comparing to extremely high quality calculations.
The key distinction between something being an approximate theory and a
semiempirical model is whether it has a clear physical motivation and connection.

### Advantages
  - broader applicability than empirical methods
  - significantly faster than first principles (100-1000 times faster)
  - can be quite accurate for the types of problems for which it was designed
  
### Disadvantages
  - difficult to rationalize about errors or inaccuracies
  - cannot approach "spectroscopic accuracy"
  
### Example: Hückel Theory
  - basic equations have a similar form as DFT
  - designed to give reasonable electronic orbitals, NOT energies
  - computations on 1000s of atoms is routine
  
## Empirical

Empirical models take an even bigger leap away from fundamental laws and
fully parameterize the model from empirical experience or motivation.
Once again, it's important to note that does not necessarily mean fully
from experiment. One could make a fully empirical model that is designed purely
from high quality computational results (and indeed, people do).

### Advantages
  - highly specialized so high quality results can be obtained for the right
  systems
  - often 100-1000 times faster than semiempirical models

### Disadvantages
  - requires some knowledge of the system and result before running the calculation
    - for example, for a totally new class of molecules, one would need to make a brand new empirical model just for that molecule
  - not generalizable
    - for example, empirical models used successfully for DNA are often complete trash when applied to RNA
    
### Example: Molecular Mechanics
  - molecule modeled as balls connected by springs
    - balls (atoms) have fixed atomic charges
  - requires unique parameters for each spring
    - for example, need different bond distance and spring constants
    for a C-O bond than for a C=O bond
    - in fact, will often need different parameters for the C-O spring in
    an ether than in an alcohol.
  - MM calculations with millions of atoms is pretty routine now
