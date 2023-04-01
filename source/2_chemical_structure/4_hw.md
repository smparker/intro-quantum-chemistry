# HW 2

## Build Structures

For each of the molecules listed and shown below:

- use Avogadro to build the structure shown (taking care of stereochemistry)
  and generate an image of the structure by exporting from Avogadro
- report the distance (Angstrom) between the two labelled atoms in each molecule

1. bicyclo[2.2.2]octane
2. camphor
3. glucose
4. porphyrin

## Conformer Search

Use CREST to find the most likely conformers of the alanine-alanine dipeptide (alala).

- Build alala using whatever method you like. Helpful hint: TmoleX has
  a built in library of amino acid structures that you can use.
- Run CREST using the default parameters. Be patient. Expect the calculation to
  take about an hour in total.
  
Use the results to answer the following questions:

1. How many conformers were found to be within 3 kcal/mol of the lowest
energy conformer?
2. What is the energy difference between the lowest energy conformer and the
next lowest energy conformer according to XTB? Give your answer in kcal/mol.
3. What are the values of the two backbone dihedral angles for each of
the alanine units in the "crest best" structure? These are angles typically plotted in a Ramachandran plot.
For consistency, be sure to measure starting from the N-terminus.

## Diels-Alder structures

Build structures for each of the reactants and products shown in the
Diels-Alder reactions below. **Save these results as they will be used
in the first full lab**. For each molecule (2 reactants and 2 products)

- Optimize the geometry using the TPSS density functional and the def2-SVP basis set
- Verify they are minima by computing the vibrational frequencies
- Report the energies and lowest frequency vibrations for each molecule
- Report the reaction energies in kcal/mol