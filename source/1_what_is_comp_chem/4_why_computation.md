# Why computation?

Before we get deep into the details of different types of theories and their computational
costs, we need to back up and talk about why we do computation in the first place.
More specifically, we need to be able to answer the question of what is the advantage of
doing some computation instead of doing an experiment.
Let’s remind ourselves what the overarching goal of chemistry is in the first place.

## The central science

The wikipedia definition of chemistry is

> the scientific discipline involved with elements and compounds composed of atoms,
> molecules and ions:
> their composition, structure, properties, behavior, and the changes they undergo during a
> reaction with other substances.

So for any technique to be valuable to the field of chemistry it should

- be concerned with atoms, molecules, and ions
- tell us something about their
  - composition: what elements are present in a substance?
  - structure: how are the elements arranged, bonded, etc.?
  - properties: mass, color, volume, charge, dipole, etc.?
  - behavior: what happens in the presence of heat, pressure, etc?
  - reactivity: how does it change when exposed to other substances, light, materials, etc.?

## Computation and the central science

Almost every one of these foundational aspects of chemistry can be probed either directly
or indirectly using computational techniques.
We will see many of these examples first hand.
Here are just a few of the most common questions we answer computationally (from Jensen).

- Which geometrical arrangements of the nuclei correspond to stable molecules?
- What are their relative energies?
- What are their properties (dipole moment, polarizability, NMR coupling constants, etc.)?
- What is the rate at which one stable molecule can transform into another?
- What is the time dependence of molecular structures and properties?
- How do different molecules interact?

Can you classify each question in terms of which of the fundamental aspects of chemistry
it addresses?

## When is computation advantageous?

A common aphorism across all of science is

> All models are wrong, but some are useful.

In other words, we should not expect computation to ever be a complete replacement for a
good experiment.
So why is computation so useful?
There are three main advantages to computation that make it a wonderful complement to
experiments.

### 1. Computation directly provides details unobtainable from experiment

Think about the molecule ethanol.
By now, you have built enough chemical intuition through your studies that you can
immediately tell many important properties of ethanol, including its polarity:
Ethanol is slightly polar because there is a slight negative charge on O and a slight
positive charge on the alcoholic H.

But how was this determined first?
Did you look at ethanol with a really powerful microscope and count the number of
electrons on the oxygen?
Experimentally, this is an absurd question.
But not computationally.

This is the single biggest advantage of doing computation:
whereas experiment tends to provide indirect evidence, theory can directly estimate
quantities that are inherently unobservable but that are vital to our understanding of
chemical structure and reactivity.
A friend of mine that completed a PhD doing synthetic inorganic chemistry before becoming
a computational chemist described it to me like this

> When you run an experiment, you know you’re seeing something real, you just don’t know
> what it means.
> When you do computation, you know exactly what you’re simulating and what it means, you
> just don’t know how real it is.

### 2. You have control over simulations that are difficult or impossible to achieve in an experiment

Put simply, you can simulate “experiments” in a computer that would be difficult or
impossible to perform in the real world.
For an extreme example, what if you wanted to know how chemistry would change if electrons
suddenly became 10 times heavier.
Experimentally, we can not adjust the mass of the electron.
But you can in the computer. 

### 3. Experiments are sometimes dangerous or expensive

There’s nothing better than a high quality experiment.
But as many of you are already aware, science is hard.
High quality experiments are not always available for one reason or another.
For example, sometimes

- the experiment is dangerous (radioactive, combustible, etc.)
- the experiment is expensive or laborious
- the required materials or equipment are inaccessible
  - like during a pandemic!

In all of these cases, you would most likely use computation to reduce the need for the
dangerous, expensive, or inaccessible experiments.
For example, suppose you are looking for a small molecule drug that will inhibit a certain
protein. The most rigorous way to determine whether any given drug works is to synthesize
it, purify it, and then test it on a living organism.
How long do you think it will take you to synthesize every possible organic molecule ever
reported in the literature?
In 2012, that number was pegged at around
[60 million](https://pubs.acs.org/doi/pdf/10.1021/ci300415d).

Instead, you could use computation to *screen* those 60 million molecules and pick some
manageable number to test manually, say a few hundred.

### Experiment and theory are symbiotic

For the above reasons, the best approach is to consider experiment and computation to be
two complementary approaches to understanding chemistry.
Theory/computation can guide experiment by 1) providing detail inaccessible from
experiment, 2) allowing for control of “experiments” that would not be possible in the
real world, and 3) replacing or supplement experiment when they are prohibitive for cost
or safety reasons.
Meanwhile, good experiments point to flaws in fundamental
theories and can therefore improve models.

Think of computation like any other instrumental technique that has its own unique
advantages and disadvantages.
