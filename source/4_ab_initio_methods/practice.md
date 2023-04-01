
# Cooking up some Big O Notation

## a. Farewell!

1. Imagine you’re in a meeting with $N$ participants.
   Suppose that before ending the meeting, every participant **must** shake the hand of every
   other participant.
   What is the Big O scaling of this farewell?
2. Come up with “farewell algorithms” that have linear and constant scaling.

## b. Noodles

1. Design an algorithm for cooking noodles (i.e., boiling in water) that scales constantly
   with the amount of pasta.
   What equipment would you need to pull that off?
2. Design an algorithm for cooking noodles that scales linearly with the amount of pasta.
   What equipment would you need to pull that off?
3. Can you think of when you’d want to use algorithm 2 instead of algorithm 1?

## c. Estimate Cost

Suppose that calculating the energy of a single water molecule requires 1 minute using
your favorite quantum chemistry method.
How much time would it take to compute the energy of a water cluster with 2, 5, or 10
molecules if your favorite method scaled linearly, quadratically, or with the sixth power
of the number of water molecules.
Answer by filling in the table below.
In otherwords, for each column, assume the method has the given scaling and estimate how
much time it would take to compute 2, 5, and 10 water molecules.


$$N$$ water molecules in cluster | $$\mathcal{O}(N) = N$$ | $$\mathcal{O}(N^2)$$ | $$\mathcal{O}(N^6)$$
-------------------------------- | ---------------------- | -------------------- | --------------------
1                                | 1 min.                 | 1 min.               | 1 min.
2                                |                        |                      |
5                                |                        |                      |
10                               |                        |                      |

The method CCSD(T) is often referred to as the “gold standard” method in quantum
chemistry. CCSD(T) scales with $\mathcal{O}(N^7)$. Using the same assumptions as above (computing 1 water
molecule takes 1 minute), how many water molecules could you include in your calculation
if you wanted your calculation to finish before you graduate from CWRU?
