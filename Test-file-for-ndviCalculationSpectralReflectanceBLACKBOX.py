# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:21:27 2020

@author: robin
"""
" TEST FILE FOR ndviCalculationSpectralReflectanceBLACKBOX "
# Use valid .csv (comma separated values) file containing spectral data from ASD (ViewSpecPro ASCII Export)
# Ex. csv file = Paul_20200527.csv

from ndviCalculationSpectralReflectanceBLACKBOX import ndviSpectralReflectance

ndviSpectralReflectance('Paul_20200527.csv')

# output = Paul_20200527_reflectance.xlsx

# For test, use these column values for points:
# point 1 = 77 78 79 80 81
# point 2 = 72 73 74 75 76

# The white board column for each is column 1
