# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 10:42:18 2020

@author: robin
"""
" Blackbox Version of ... "
" NDVI Calculation from Raw DN TXT --> EXCEL File "

def ndviSpectralReflectance(fileName):
    import pandas as pd
    import os
    
    done = False
    while not done:
        try:
            df = pd.read_csv(fileName)
            done = True
        except IOError: 
            print("Please enter a valid .csv file.")
            break
        except ValueError: 
            print("File contents invalid. Please enter a valid .csv file.")
            break
        
    # Retrieved from: https://pbpython.com/selecting-columns.html
    col_index = [f"{c[0]}:{c[1]}" for c in enumerate(df.columns)]   
    print(col_index)    # This allows the user to see the column #'s. User will have
    # to manually input column range for each sample point and program will create
    # a new column for average and spectral reflectance
    
    # POINT 1
    point_01_cols = input("Enter the column index numbers for sample point 1 (with a space between each column #): ")
    w1_01_cols = list(point_01_cols.split())
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    point1 = [int(i) for i in w1_01_cols]       # This is list comprehension
    # This given us the integer version of the original string list
    
    # Now I want to take an average of each row (ex. wavelength 325) over the columns
    # need to average rows 0:750
    # How to average for each row: df.mean(axis=1): From: https://datatofish.com/average-column-row-dataframe/
    w1_01 = df.iloc[:, point1]
    row_avg_1 = w1_01.mean(axis=1)
    refl1 = input("Specify column # representing whiteboard reflectance for point 1: ")
    refl1 = list(refl1)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl1 = [int(i) for i in refl1]       # This is list comprehension
    refl1_test = df.iloc[:, refl1]
    refl1_test_2 = refl1_test.mean(axis=1)
    point1_reflectance = (row_avg_1)/(refl1_test_2)
    
    # POINT 2
    w1_02_cols = input("Enter the column index numbers for sample point 2 (with a space between each column #): ")
    w1_02_cols = list(w1_02_cols.split())
    point2 = [int(i) for i in w1_02_cols]
    w1_02 = df.iloc[:, point2]
    row_avg_2 = w1_02.mean(axis=1)
    refl2 = input("Specify column # representing whiteboard reflectance for point 2: ")
    refl2 = list(refl2)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl2 = [int(i) for i in refl2]       # This is list comprehension
    refl2_test = df.iloc[:, refl2]
    refl2_test_2 = refl2_test.mean(axis=1)
    point2_reflectance = (row_avg_2)/(refl2_test_2)

    
    # OUTPUT TO EXCEL FILE
    # https://stackoverflow.com/questions/13437727/writing-to-an-excel-spreadsheet
    excel_filename = input('Enter file name to save to (.xlsx): ')
    sheetName = input('Enter sheet name for .xlsx file: ')
    reflectance_df = pd.DataFrame({'Point 1 reflectance': point1_reflectance, 'Point 2 reflectance': point2_reflectance})
    reflectance_df.to_excel(excel_filename, sheet_name= sheetName, index=False)
    
    file_path = os.path.dirname(os.path.realpath(excel_filename))
    print("Output NDVI file", excel_filename, " has been saved to: ", file_path)
    
    
    " Calculating NDVI "

    w1_01_vis_rows2 = w1_01.iloc[255:356]
    w1_01_nir_rows2 = w1_01.iloc[400:750]
    
    w1_01_vis_av2 = w1_01_vis_rows2.mean(axis = 0)        # This calculates average of the visible rows (255-356) and outputs the VIS average
    w1_01_nir_av2 = w1_01_nir_rows2.mean(axis = 0)        # Does the same but with NIR
    
    w1_01_ndvi = ((w1_01_nir_av2 - w1_01_vis_av2) / (w1_01_nir_av2 + w1_01_vis_av2))
    #print(w1_01_ndvi)
    
    ndvi_avg_01 = sum(w1_01_ndvi) / len(w1_01_ndvi)
    print(ndvi_avg_01)
    
    #w1_01_ndvi_list = []
    #for value in w1_01_ndvi:
        #w1_01_ndvi_list.append(value)
        #print(w1_01_ndvi_list)
    #w1_01_ndvi_avg = sum(w1_01_ndvi_list) / len(w1_01_ndvi_list)
    
    w1_02_vis_rows2 = w1_02.iloc[255:356]
    w1_02_nir_rows2 = w1_02.iloc[400:750]
    
    w1_02_vis_av2 = w1_02_vis_rows2.mean(axis = 0)        # This calculates average of the visible rows (255-356) and outputs the VIS average
    w1_02_nir_av2 = w1_02_nir_rows2.mean(axis = 0)        # Does the same but with NIR
    
    w1_02_ndvi = ((w1_02_nir_av2 - w1_02_vis_av2) / (w1_02_nir_av2 + w1_02_vis_av2))
    w1_02_ndvi_list = []
    for value in w1_02_ndvi:
        w1_02_ndvi_list.append(value)
        print(w1_02_ndvi_list)
    w1_02_ndvi_avg = sum(w1_02_ndvi_list) / len(w1_02_ndvi_list)
    print(w1_02_ndvi_avg)
    
    ndvi_df = pd.DataFrame({'Point 1 Avg NDVI': ndvi_avg_01, 'Point 2 Avg NDVI': w1_02_ndvi_avg}, index=['ndvi'])
    ndvi_filename = input("Enter name of file for NDVI output (.xlsx format): ")
    ndvi_sheetname = input("Enter sheetname for ndvi, .xlsx file: ")
    ndvi_df.to_excel(ndvi_filename, sheet_name= ndvi_sheetname, index=True)
    file_path_ndvi = os.path.dirname(os.path.realpath(excel_filename))
    print("Output NDVI file", ndvi_filename, " has been saved to: ", file_path_ndvi)