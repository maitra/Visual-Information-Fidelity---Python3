# Visual-Information-Fidelity (VIF) - Python3

This repository contains Python3 implementation of the steerable pyramid version of Visual Information Fidelity (VIF) proposed in [1]. This is a fork of the original Python2 code that was a replicate of the MATLAB code released by the authors of [1] which is available [HERE](http://live.ece.utexas.edu/research/Quality/ifcvec_release.zip).

## Dependencies
1) Python (>=3.5)
2) Numpy (>=1.16)
3) Python Imaging Library (PIL) (>=6.0)

I needed python-PyQt4, pypy-libs (for tkinter), python3-matplotlib, python3-imaging, python3-scipy and python-numpy packages from Fedora's repositories.

The use of this code needs compilation of three C programs into a shared object:

gcc -c -fPIC  convolve.c wrap.c edges.c -std=c17 -Wall -pedantic

and building the shared library:

gcc -shared -o wrapConv.so convolve.o edges.o wrap.o

## Usage
Let imref and imdist denote reference and distorted images respectively. Further, let sigmasq be the noise variance, and M be the size of the block (to give a MxM block).  Then the VIF value is calculated as
VIF = vifvec(imref, imdist, sigmasq, M)


A demo code is provided in test.py for testing purposes with some example datasets:

_python3 ./test.py ultadanga.tiff ultadanga-64-rgb.png 1 7
This yields: _0.8014978518810658



[1]H.R. Sheikh, A.C. Bovik and G. de Veciana, "An information fidelity criterion for image quality assessment using natural scene statistics," IEEE Transactions on Image Processing , vol.14, no.12pp. 2117- 2128, Dec. 2005.
