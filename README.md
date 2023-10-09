# Visual-Information-Fidelity (VIF) - Python3

This repository contains python implementation of steerable pyramid version of Visual Information Fidelity (VIF) proposed in [1]. This is a fork of the original Python2 code that was a replication of MATLAB version released by the authors of [1] which is available [HERE](http://live.ece.utexas.edu/research/Quality/ifcvec_release.zip).

## Dependencies
1) Python (>=3.5)
2) Numpy (>=1.16)
3) Python Imaging Library (PIL) (>=6.0)

I needed python-PyQt4, pypy-libs (for tkinter), python3-matplotlib, python3-imaging, python3-scipy and python-numpy packages from Fedora's repositories.

## Usage
Let imref and imdist denote reference and distorted images respectively. Then the VIF value is calculated as
VIF = vifvec(imref, imdist)

A demo code is provided in test.py for testing purposes

[1]H.R. Sheikh, A.C. Bovik and G. de Veciana, "An information fidelity criterion for image quality assessment using natural scene statistics," IEEE Transactions on Image Processing , vol.14, no.12pp. 2117- 2128, Dec. 2005.
