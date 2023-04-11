---
myst:
  substitutions:
    markov_shell: |
      :::{image} /_static/markov-shell-access.png
      :height: 2em
      :::
    markov_desktop: |
      :::{image} /_static/markov-desktop.png
      :height: 2em
      :::
---
# Modern High Performance Computing Systems

Modern High Performance Computing (HPC) clusters typically
have at least two types of servers in the cluster:

-   **compute nodes** are the powerful computing machines that will run
    the actual calculations
-   **head nodes** are lightweight servers that act as
    gateways from the outside world to the compute nodes

For example, the markov cluster at CWRU has this arrangement.
It is important to use these correctly.

## Head nodes

When you first log into markov either through
`ssh -Y <caseID>@markov.case.edu`, through the {{markov_shell}}
tab in ondemand, or using X2Go, you are connecting directly
to the head node. In reality, `markov` and `rider` are not really
servers by themselves but gateways to a collection of headnodes. When
you log into `markov` or `rider`, you are somewhat randomly assigned you
to an individual headnode. Headnodes on the CWRU HPC system are named
things like `hpc1`, `hpc2`, etc. The number one rule on the head node is
**DO NOT RUN DEMANDING PROGRAMS ON THE HEAD NODE.** The only commands
you should run directly on the head node are things like making
directories, moving files around, and setting up some simple
calculations. A useful rule of thumb is that if you\'re going to wait
for more than a *few seconds* for the result of a command, you should
run the command on a compute node. To get a compute node from the head
node, run

    srun --account smp201_chemx42 --partition classc -N 1 -n 1 -c 2 --time=1:00:00 --mem=5gb --pty /bin/bash

If you logged in using x2go and you want the compute node to be able to
show graphics, you will need to use

    srun --x11 --account smp201_chemx42 --partition classc -N 1 -n 1 -c 2 --time=1:00:00 --mem=5gb --pty /bin/bash

That submits an \"interactive job\" to the queue. Once the interactive
job starts, you will have access to a normal compute node on which you
can run whatever calculations your heart desires. You can also adjust
your time and memory requirements in the above command by adjusting the
`--time=<time>` and `--mem=Xgb` options.

## Compute nodes

If you login to markov using the ondemand {{markov_desktop}}, then you start
off on a compute node. Otherwise, you need
to request a compute node as detailed above. Pretty much all nontrivial
calculations you ever run should be on a compute node. Research compute
nodes (rider) have names like `compt0123`, and educational (markov) have
names like `classct001`.
