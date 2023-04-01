# Accuracy is always relative to what you need

Rather than thinking about some methods as being "good" and some as
being "bad", we will try to classify different methods as we come
to them in terms of _what they are and are not good at_. Another way of
putting this is that you should always think of a method's accuracy and
precision relative to what you need out of the calculation.

For now, pay the most attention to how to characterize the errors. We will
discuss the individual methods as we use them.

Note: The accuracy vs precision distinction in the case of computation
is a little ambiguous for simple reason that if I run the same calculation
twice (i.e., repeat an experiment), I will typically get the same
exact number back up to some ridiculous number of digits. Therefore, I
find it more convenient to think in terms of systematic errors and
quantitative errors.

## Systematic errors (accuracy)

Many methods will exhibit systematic errors with respect to certain
types of interactions of chemical species. Common examples include:

  - dispersion energies like van der Waals forces
    - some methods lack dispersion (Hartree-Fock or HF)
    - some methods over estimate dispersion (Second-order
      Møller-Plesset Perturbation Theory or MP2)
  - many methods do not incorporate effects of relativity
    - no spin-orbit coupling
  - some methods may overestimate or underestimate hydrogen bonding
  - some methods may produce consistently wrong spectra
  
Systematic errors in methods are actually a lot easier to deal with,
because we can try to be aware of where the systematic errors will creep in
and then just avoid using methods that we _know_ will give awful results.
For example, if we want to predict UV absorption spectra, we make sure we
choose a method that does not suffer from any well known deficiencies
in predicted spectra.

## Quantitative errors (precision)

Quantative errors in this context are the expected difference between a
computed result and the exact result. These errors are determined by
i) doing calculations on huge databases of molecules and ii) comparing them
to either high quality experiment or high quality calculations. Think of
these as the numerical part of statements like

  - I expect the computed reaction energy to be within 1 kcal/mol of the exact value
  - I expect bond the computed bond lengths to be within about 1 pm of the exact value
  
These tell us rough confidence bounds for specific results.

That said, often **relative** results can be significantly more reliable than
one would expect based on these quantitative errors. We'll discuss examples
of this when we start computing reaction energies in class.
