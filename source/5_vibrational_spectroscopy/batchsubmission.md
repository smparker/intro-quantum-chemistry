# Batch Submission on Markov

Most of the time that computational scientists are running calculations,
they are in fact not doing it interactively (as we have been doing in
this course). There is a really simple reason for this: who wants to sit
and wait for a week for a calculation to run? Instead, we use what is
called batch submission to run calculations noninteractively. The
details change from HPC system to HPC system, but the basic way it works
is that you will run a command like

    sbatch -C turbomole_job.slurm

where the program sbatch talks to the queue system on the HPC
environment and the file turbomole_job.slurm is a script (really just a
text file) that tells the queue system the details of the job to be run
(how many processors to use, how long to run, what machines to use,
etc.) and then contains the commands to be run. CWRU uses the Slurm
queue system so submission scripts are referred to as \"Slurm scripts\".
The most barebones submission script you could imagine would look like
this

    #!/bin/bash
    #SBATCH -o test.o%j
    #SBATCH --time=00:30:00      # 30 minutes of wall time
    #SBATCH -N 1         # 1 Node
    #SBATCH -n 1         # 1 processor
    #SBATCH -mem=2gb     # Assign 2gb memory; default in 1gb

    module load <software-module>
    run_calculation

The first line just specifies that this file will be run as a script.
The lines at the top that look like `#SBATCH -n 1` are specifying
options to the queueing system. Everything from the module load below is
the list of commands that will be run once your calculation starts.

## Turbomole submission

Writing your own submission script is easy enough, but it turns out you
won\'t have to in this class, because there is a simple enough script
that will automatically generate and submit a script for a job. First,
verify you have access to the `turbomole_submit` script by running
`turbomole_submit -h`. You should see

    [smp201@hpc5 ~]$ turbomole_submit -h
    turbomole_submit: turbomole submission helper
    Submission script helper for running turbomole on rider/markov.
    Features:
      - copies calculation to scratch directories before running

    usage:
      turbomole_submit [options] <command(s) to run>

    Note: you MUST be in the directory of the calculation to be run
    Warning: make sure there are no nested directories actively running
             calculations at the same time as this submitted job. Due
             to the way data is copied back, data in nested folders
             may be overwritten!
    SLURM parameters:
      -c,--cpus-per-task fill SLURM cpus-per-task
      -J,--job-name      fill SLURM job name
      -m,--mem           fill SLURM memory per node
      --mem-per-cpu      fill SLURM memory per cpu
      -N,--nodes         set number of nodes to use
      -n,--ntasks        set total number of tasks to spawn
      --ntasks-per-node  set total number of tasks to spawn per node
      -t,--time          requested wall time
      -a,--account       account to use
      -p,--partition     partition to use

    Generation parameters:
      -s,--no-submit     do not automatically submit generated script

    Special:
      -C,--chemx42       automatically set up for CHEM342/442

      -h,--help          print this message and exit

This summarizes the usage and options for this script, but we'll walk
through the basics now. The first important point is that you need to
use the `-C` option in the `turbomole_submit` script because that
sets everything up to work automatically with the course.
The really simple idea is that if you run

    turbomole_submit -C 'jobex > jobex.out'

then the script will automatically generate a slurm submission file
(called `turbo.slurm`) that sets up and runs the command
`jobex > jobex.out`. It has a few nice features, such as that it will
automatically copy the input files to a temporary directory (which is
much faster) and then copy back when the calculation is done.

WARNING: The quotation marks for the command are important! For example,
if you run

    turbomole_submit -C jobex > jobex.out

then the slurm file that gets made only runs the command `jobex` and it
won\'t capture the output. This means you could run your calculation and
then lose the results! If this happens, not all hope is lost though,
there is usually a slurm output file that will contain ALL of the output
from the entire job, not just the turbomole output.

WARNING: Do not use the `nohup ... &` pattern in a submission script.
The `&` means the command will run in the background and the submission
script will move on and then finish running through the rest of the
script. Once that happens, the job is killed, no matter what status it
is!

In this course, you won\'t need to update most of the options, but I do
want to mention two that are important. The `-t` option will let you
change the amount of time the job will run for. The default amount of
time is 12 hours. This is plenty for almost every job you\'ll run in
this class. But if you want to make it longer, you can use the option
`-t 1-08:00:00`, which, for example, sets the length of the job to be 1
day and 8 hours.

The other important option is the `-s` option. When you provide -s to
the script, it will generate the slurm file and then stop. So if you
would like to use this script to generate a file and then edit it
manually, use the `-s` option. That would look like

    turbomole_submit -C -s

This will then make a slurm file called `turbo.slurm`. When `-s` is
provided, giving an actual command is now optional because the script
expects you to go through and edit the submission script manually. If
you edit it manually and then want to submit it to the queue, you can
run

    sbatch turbo.slurm

Finally, once your job is running you can check it\'s progress by using
the command

    squeue -u <username>

For example, I run `squeue -u smp201` and I might see the output

                 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
              15207814     batch    turbo   smp201  R      12:43      1 compt255

which tells me I have one job in the queue system

-   with ID `15207814`
-   running on the `batch` partition
-   the job name is `turbo`
-   the job is actively running (`R`)
-   and has been for 12 minutes and 43 seconds
-   it is using `1` node
-   and that node is named `compt255`

The other most common status you'll see is `Q`, which means it is
queuing (waiting to start).
