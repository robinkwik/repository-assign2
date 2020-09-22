# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:15:07 2020

@author: robin
"""

" NDVI Calculation from Excel as a function "

def ndviCalculation(fileName):
    import pandas as pd
    import os
    df = pd.read_csv(fileName)
    
    col_index = [f"{c[0]}:{c[1]}" for c in enumerate(df.columns)]
    
    refl_index = []

    for column in col_index:
        if 'Reflectance' in column:
            refl_index.append(column.split(':')[0])
    
    integers = list(map(int, refl_index))
    
    columns = df.columns.ravel()
    
    columns_refl = [string for string in columns if "Reflectance" in string]
    if "Soil Reflectance" in columns_refl:
        columns_refl.remove("Soil Reflectance")
    
    sig_col_refl = df.iloc[:, integers]

    # Select rows by position
    vis_rows2 = sig_col_refl.iloc[255:356]
    nir_rows2 = sig_col_refl.iloc[400:750]
    
    vis_av2 = vis_rows2.mean(axis = 0)        # This calculates average of the visible rows (255-356) and outputs the VIS average
    nir_av2 = nir_rows2.mean(axis = 0)        # Does the same but with NIR

    ndvi_cobban80_automated = ((nir_av2 - vis_av2) / (nir_av2 + vis_av2))     # Calculates NDVI
    
    # Now we can output to an excel file!
    file_output = input("Enter output excel file name (.xlsx format): ")
    ndvi_cobban80_automated.to_excel(file_output)
    file_path = os.path.dirname(os.path.realpath(file_output))
    print("Output NDVI file", file_output, " has been saved to: ", file_path)
