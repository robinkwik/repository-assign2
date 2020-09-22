# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 09:03:18 2020

@author: robin
"""

" PROGRAM FOR CALCULATING NDVI FROM EXCEL FILE WITH SPECTRAL REFLECTANCE "
# Let's try selecting columns using pandas and numpy
# https://pbpython.com/selecting-columns.html
import pandas as pd
import numpy as np 
import os

# Test file = Cobban80_0505-test.csv

# df = dataframe... name of csv is: 
file = input("Enter name of file (.csv format): ")
df = pd.read_csv(file)

# List comprehension method borrowed from the above link in order to index rows & columns
col_index = [f"{c[0]}:{c[1]}" for c in enumerate(df.columns)]
print(col_index)
# enumerate function: https://book.pythontips.com/en/latest/enumerate.html
# This is the output: ['0:Wavelength', '1:(WB) W300000.asd', '2:W300001.asd', 
# '3:W300002.asd', '4:W300003.asd', '5:W300004.asd', '6:W300005.asd', '7:Soil Avg', 
# '8:Soil Reflectance', '9:W300006.asd', '10:W300007.asd', '11:W300008.asd', 
# '12:W300009.asd', '13:W300010.asd', '14:W3_01 Avg', '15:W3_01 Reflectance',
# '16:W300011.asd', '17:W300012.asd', '18:W300013.asd', '19:W300014.asd'] etc...

# From the 'col_index' variable, I found the columns I need 

# df.iloc[:,[1,2,5]]
# This selects columns in positions 1, 2 and 5 (first column is 0).



#sig_col = df.iloc[:,[0, 15, 23, 30, 37, 44, 51, 58, 65, 72, 79, 86, 93, 100, 107, 114, 121]]
# this selects the reflectance columns, but we have to manually input them... 
# LETS AUTOMATE THIS!
# So now, wavelength remains column 0, and w3_01 is column 1. So each column corresponds 
# to sample point number

# This works! but I want to automatically choose the columns rather than input them

refl_index = []

for column in col_index:
    if 'Reflectance' in column:
        refl_index.append(column.split(':')[0])
        print(refl_index)

integers = list(map(int, refl_index))       # https://www.techiedelight.com/convert-list-of-string-into-list-of-integers-python/
print(integers)


" START OF TEST "

columns = df.columns.ravel()
print(columns)

columns_refl = [string for string in columns if "Reflectance" in string]       #this works
if "Soil Reflectance" in columns_refl:      #This works as well to remove soil refl
    columns_refl.remove("Soil Reflectance")
    print(columns_refl)


print(df.columns)
sig_col_refl = df.iloc[:, integers]
print(sig_col_refl)

# Select rows by position
vis_rows2 = sig_col_refl.iloc[255:356]
nir_rows2 = sig_col_refl.iloc[400:750]
print(vis_rows2)
print(nir_rows2)

vis_av2 = vis_rows2.mean(axis = 0)        # This calculates average of the visible rows (255-356) and outputs the VIS average
nir_av2 = nir_rows2.mean(axis = 0)        # Does the same but with NIR
print(vis_av2)
print(nir_av2)

ndvi_cobban80_automated = ((nir_av2 - vis_av2) / (nir_av2 + vis_av2))     # Calculates NDVI
print(ndvi_cobban80_automated)

# Now we can output to an excel file!
file_output = input("Enter output excel file name (.xlsx format): ")
ndvi_cobban80_automated.to_excel(file_output)

" END OF TEST "

