# boundaryConditions generated for growing mesh on a displacement solid mechanics solver

Given two .stl surfaces alligned and concentric we need to find the normal vectors from the small surface to the big surface

Surface info is handled by pyvista.
## Requirements
```
pip install pyvista
pip install numpy
````
## Usage
Change the filenames on:
```
meshBigFile = 'BC/E13_outer.stl'
meshSmallFile = 'BC/E15_outer.stl'
```
