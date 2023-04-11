# How To: Build a Molecule in Avogadro

In this exercise, we will use the program [Avogadro](https://avogadro.cc/) to
construct 3D representations of molecules. As a motivating example, let's build
a 3D representation of phenol.

## Open Avogadro

1. Launch a GUI based desktop session on markov
2. Open a Terminal
3. Run
:::{code-block} console
module load gcc/6.3.0
module load avogadro
avogadro
:::

You should now see the opening Avogadro window, which should look something
like this. (If you're having problems getting this to work, try downloading the
program straight from the avogadro website for macOS or windows).

:::{image} /_static/avobuild_01_empty.jpg
:::

## Build phenol

1. Select the build tool
:::{image} /_static/avobuild_02_click_build.gif
:::
2. Click on the black box to place a carbon atom. Click and drag from the first atom to make another atom with a single bond

:::{image} /_static/avobuild_03_click_carbon.gif
:::

3. Click on a bond to make it a double bond
:::{image} /_static/avobuild_04_make_double.gif
:::

4. Select "Oxygen" from the element dropdown and click on an existing atom to turn it into an oxygen atom
:::{image} /_static/avobuild_05_make_oxygen.gif
:::

5. Finish the ring by clicking and dragging to make new carbon atoms, and turning select bonds into double bonds
:::{image} /_static/avobuild_06_finish_ring.gif
:::

6. Preoptimize using the MMFF94 force field by finding the optimize symbol in the toolbar (E), selecting the MMFF94 force field, and clicking start
:::{image} /_static/avobuild_07_preoptimize.gif
:::

7. Click the measure button (looks like a ruler). Click two atoms to measure the distance. Click a third to measure an angle. Click a fourth to measure a dihedral.
:::{image} /_static/avobuild_08_measure_distance.gif
:::

8. Made a mistake? Delete atoms by right clicking on the atom.
:::{image} /_static/avobuild_12_delete.gif
:::

## Save an xyz

9. Select "Save As..."
:::{image} /_static/avobuild_09_save_as.gif
:::

10. Save in "xyz" format, which is probably the most flexible and widely used
:::{image} /_static/avobuild_10_xyz.gif
:::

11. Rotate your view by clicking the cross-like button
:::{image} /_static/avobuild_11_rotate.gif
:::

## Tips for better images
12. Remove the axes
:::{image} /_static/avobuild_13_axes.gif
:::

13. Set background to be white
:::{image} /_static/avobuild_14_background.gif
:::

14. Save to png
:::{image} /_static/avobuild_15_export.gif
:::



