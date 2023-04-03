# Algorithms

The types of computation we'll be dealing with in this class is the solution
of equations motivated by theory. In other words, theory tells us the equations
that need to be solved and then we use the computer to solve the equations.
To actually solve the equations, we use "algorithms". Algorithms are
just the series of steps one takes. For example, a cooking recipe is
an algorithm.

## The cost of algorithms
In this class, we will use a bunch of different computational methods
that vary in terms of their accuracy and their computational cost.
As I've mentioned before, all scientific computing comes down to
the question of "how much accuracy/realism do you need and how much
are you willing to pay (computationally, of course) to get it".
Therefore, we need some way to talk about the cost of algorithms.
To do that we use Big O notation.

### What is Big O notation? (required)
Watch the following video introduction to algorithms

:::{youtube} MyeV2_tGqvw
:::

Big O tells us about the asymptotic scaling of an algorithm,
meaning how does the amount of time/memory/disk/etc. the algorithm
requires change as the inputs get larger and larger. For example,
let's say that you're making sandwiches and you can reliably make
1 sandwich every 5 minutes. Then the amount of time it takes you to make
$n$ sandwiches is 5 minutes $\times n$. This means the sandwich making
algorithm is a $\mathcal{O}(n)$ process.

  - what would the Big O scaling of the sandwich making process be if
  for every sandwich you made, you threw one out?
  - what would the Big O scaling of the sandwich making process be if
  you had a friend helping you to make sandwiches at the same rate?
  - what would the Big O scaling of the sandwich making process be if
  you first ran $n$ miles before making your $n$-th sandwich?
  - what is the best sandwich?

One important point to keep in mind is that the solution to the equations
and the algorithm to get you that solution are two different things.
That's important to keep in mind because not all algorithms are
created equally.
This sometimes gets confusing in computational chemistry because
we (the community) have a habit of talking about **theories**
in terms of their cost, when really what we mean is that the
best known algorithms to arrive at solutions to those theories
has a particular cost.
