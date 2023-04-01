# Computational Chemistry is an example of Scientific Computing

Most of your experience in chemistry so far has been a mix of experimental and theoretical. So what exactly is _computational chemistry_? To answer this, we need to clarify a bit what I mean by experiment and theory.

- **Chemical theory** is the collection of all the stories we tell ourselves about why atoms, molecules, or materials behave the way we do. Think about things like the kinetic theory of gasses (from which you can derive the famed $PV=nRT$ ideal gas law equations) or even Newton's equations of motion.
- **Experimental** chemistry is the collection of all the skills, tools, and knowledge around the practice of empiricism in chemistry. Experiment is how we arrive at statements like Boyle's law, which relates the temperature of an ideal gas to the volume it occupies.

Depending on your point of view, computational chemistry can be both, either, or neither of these. More commonly, computational chemistry is connected to chemical theories where the math involved is too complicated to solve analytically, so computers are used to help out.

Let's think about an example from kinetics. Suppose we know that the following reaction is first-order

\begin{equation} A \rightarrow B \end{equation}

We know that first-order kinetics follow the differential equation

\begin{equation}
\frac{d[A]}{dt} = - k [A].
\end{equation}

If all we need to know is the concentration of $[A]$ across time, then we can solve this exactly as

\begin{equation}
[ A ] (t) = [A]_0e^{-kt},
\end{equation}

and we're pretty much done. This is an example of an analytically solvable problem. Let's suppose instead we had a many possible reactions.

\begin{align}
A &\rightarrow B \\
B &\rightarrow C + D \\
D + A &\rightarrow E \\
E + B &\rightarrow C + D
\end{align}

I don't care how smart you are, you won't be able to write down an equation showing the concentration of $[C]$ as a function of time for any set of starting concentrations. A computer, on the other hand, could solve this numerically without much problem at all. That is the basic idea behind scientific computing.

**Scientific computing** is the branch of scientific research that uses advanced computational resources to study scientific problems. More specifically, **computational chemistry** is the "branch" of chemistry that uses high performance computing to solve chemical problems. In the general sense, it does not matter whether those problems come from interpreting experiment or from applying chemical theory. That said, if someone introduces themselves as a "computational chemist", they probably mean that they use computers to solve equations coming from theoretical chemistry.

## Some interesting history about computers

The first "computers" were people. For example, in the 18th century people used trigonometry and logarithm tables to simplify complicated calculations. But who do you think built the tables? The practice of using humans for computing continued basically up until digital computers started to outperform people in the 1960s or so. From the late 1800s up until the rise of digital computers, most computers were (severely underpaid) women. "Hidden Figures" is a great book and film that tells the story of African-American women computers that were part of the space race at NASA.

### Scientific American: The Story of NASA's Real "Hidden Figures" (optional)

<https://www.scientificamerican.com/article/the-story-of-nasas-real-ldquo-hidden-figures-rdquo/>
