# CWRU High Performance Computing: markov

We will be using CWRU's markov cluster (<https://sites.google.com/a/case.edu/hpcc/>). The first thing you need to be able to do is log into the cluster. There are a few different options that I will briefly describe.

**Note: Computers can be finicky. I can only anticipate the ways in which they will be finicky on systems that I have some experience with (macOS and Linux). If you're using any other type of computer (Chromebook, Windows, etc.) and you are having trouble getting set up, then I will do my best to help you, but it's quite likely that my first step will be Google.**

The first thing to be aware of is that the CWRU HPC center has provided lots of help for getting started. The HPC guides are much more complete than what is included in this page. For that reason, your first step should be to look at the [HPC home](https://sites.google.com/a/case.edu/hpcc/home), [HPC Quick Start](https://sites.google.com/a/case.edu/hpcc/home/important-notes-for-new-users/quick-start) guides, or at the [workshop material archive](https://canvas.case.edu/courses/3014/pages/workshop-materials-archives?module_item_id=174987).

Depending on which method you choose to log into markov, you may need to use a VPN from off campus. If you do not have VPN set up on your computer, you can find instructions at [vpnsetup.case.edu](https://vpnsetup.case.edu/).

## Using OnDemand (highly recommended)

By far the easiest way to log into the CWRU HPC system is to use the OnDemand portal at [ondemand.case.edu](https://ondemand.case.edu). OnDemand uses the university SSO, so no VPN will be needed. From there, you will be able to load a terminal or launch a desktop.

## Using your computer's built-in terminal

### Windows

Although the built-in Windows terminal isn't quite compatible with Linux, these days you can install what's called the [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install-win10). This will give you some access to a terminal and then you can more or less follow the same instructions as for Linux.

You can also use PuTTy ([video guide from HPC](https://www.youtube.com/watch?v=B1TmpcnSpr0))..

### Linux, macOS, etc.

If you're on Linux or macOS, you already have a good terminal built into your computer. Search the applications on your computer for `Terminal` (also sometimes called `Konsole` on Linux). It should show you a command line prompt like we saw in the previous pages. From there you can run the command

```
ssh -Y <username>@markov.case.edu
```

where `<username>` should be replaced with your Case ID. For example, when I log in, I run

```
ssh -Y smp201@markov.case.edu
```

The `-Y` option requests graphics forwarding. Without this option you'll still be able to log in, but you won't be able to launch any programs with a graphical user interface.

## Additional help

If you're looking for extra information or reading on HPC, CWRU has put together some really nice overview of the motivation and structure of [CWRU HPC](https://drive.google.com/file/d/0By0GTaYFOIhdbHhySUJVdnNmSEE/view).
