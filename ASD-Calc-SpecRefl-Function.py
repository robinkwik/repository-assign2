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
        except ValueError: 
            print("File contents invalid. Please enter a valid .csv file.")
        
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
    refl1 = input("Specify column # representing spectral reflectance for point 1: ")
    refl1 = list(refl1)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl1 = [int(i) for i in refl1]       # This is list comprehension
    refl1_test = df.iloc[:, refl1]
    refl1_test_2 = refl1_test.mean(axis=1)
    point1_ndvi = (row_avg_1)/(refl1_test_2)
    
    # POINT 2
    w1_02_cols = input("Enter the column index numbers for sample point 2 (with a space between each column #): ")
    w1_02_cols = list(w1_02_cols.split())
    point2 = [int(i) for i in w1_02_cols]
    w1_02 = df.iloc[:, point2]
    row_avg_2 = w1_02.mean(axis=1)
    refl2 = input("Specify column # representing spectral reflectance for point 2: ")
    refl2 = list(refl2)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl2 = [int(i) for i in refl2]       # This is list comprehension
    refl2_test = df.iloc[:, refl2]
    refl2_test_2 = refl2_test.mean(axis=1)
    point2_ndvi = (row_avg_2)/(refl2_test_2)

    # POINT 3
    w1_03_cols = input("Enter the column index numbers for sample point 3 (with a space between each column #): ")
    w1_03_cols = list(w1_03_cols.split())
    point3 = [int(i) for i in w1_03_cols]
    w1_03 = df.iloc[:, point3]
    row_avg_3 = w1_03.mean(axis=1)
    refl3 = input("Specify column # representing spectral reflectance for point 3: ")
    refl3 = list(refl3)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl3 = [int(i) for i in refl3]       # This is list comprehension
    refl3_test = df.iloc[:, refl3]
    refl3_test_2 = refl3_test.mean(axis=1)
    point3_ndvi = (row_avg_3)/(refl3_test_2)

    # POINT 4
    w1_04_cols = input("Enter the column index numbers for sample point 4 (with a space between each column #): ")
    w1_04_cols = list(w1_04_cols.split())
    point4 = [int(i) for i in w1_04_cols]
    w1_04 = df.iloc[:, point4]
    row_avg_4 = w1_04.mean(axis=1)
    refl4 = input("Specify column # representing spectral reflectance for point 4: ")
    refl4 = list(refl1)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl4 = [int(i) for i in refl4]       # This is list comprehension
    refl4_test = df.iloc[:, refl4]
    refl4_test_2 = refl4_test.mean(axis=1)
    point4_ndvi = (row_avg_4)/(refl4_test_2)

    # POINT 5
    w1_05_cols = input("Enter the column index numbers for sample point 5 (with a space between each column #): ")
    w1_05_cols = list(w1_05_cols.split())
    point5 = [int(i) for i in w1_05_cols]
    w1_05 = df.iloc[:, point5]
    row_avg_5 = w1_05.mean(axis=1)
    refl5 = input("Specify column # representing spectral reflectance for point 5: ")
    refl5 = list(refl5)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl5 = [int(i) for i in refl5]       # This is list comprehension
    refl5_test = df.iloc[:, refl5]
    refl5_test_2 = refl5_test.mean(axis=1)
    point5_ndvi = (row_avg_5)/(refl5_test_2)
    
    # POINT 6
    w1_06_cols = input("Enter the column index numbers for sample point 6 (with a space between each column #): ")
    w1_06_cols = list(w1_06_cols.split())
    point6 = [int(i) for i in w1_06_cols]
    w1_06 = df.iloc[:, point6]
    row_avg_6 = w1_06.mean(axis=1)
    refl6 = input("Specify column # representing spectral reflectance for point 6: ")
    refl6 = list(refl6)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl6 = [int(i) for i in refl6]       # This is list comprehension
    refl6_test = df.iloc[:, refl6]
    refl6_test_2 = refl6_test.mean(axis=1)
    point6_ndvi = (row_avg_6)/(refl6_test_2)
    
    # POINT 7
    w1_07_cols = input("Enter the column index numbers for sample point 7 (with a space between each column #): ")
    w1_07_cols = list(w1_07_cols.split())
    point7 = [int(i) for i in w1_07_cols]
    w1_07 = df.iloc[:, point7]
    row_avg_7 = w1_07.mean(axis=1)
    refl7 = input("Specify column # representing spectral reflectance for point 7: ")
    refl7 = list(refl7)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl7 = [int(i) for i in refl7]       # This is list comprehension
    refl7_test = df.iloc[:, refl7]
    refl7_test_2 = refl7_test.mean(axis=1)
    point7_ndvi = (row_avg_7)/(refl7_test_2)
    
    # POINT 8
    w1_08_cols = input("Enter the column index numbers for sample point 8 (with a space between each column #): ")
    w1_08_cols = list(w1_08_cols.split())
    point8 = [int(i) for i in w1_08_cols]
    w1_08 = df.iloc[:, point8]
    row_avg_8 = w1_08.mean(axis=1)
    refl8 = input("Specify column # representing spectral reflectance for point 8: ")
    refl8 = list(refl8)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl8 = [int(i) for i in refl8]       # This is list comprehension
    refl8_test = df.iloc[:, refl8]
    refl8_test_2 = refl8_test.mean(axis=1)
    point8_ndvi = (row_avg_8)/(refl8_test_2)
    
    # POINT 9
    w1_09_cols = input("Enter the column index numbers for sample point 9 (with a space between each column #): ")
    w1_09_cols = list(w1_09_cols.split())
    point9 = [int(i) for i in w1_09_cols]
    w1_09 = df.iloc[:, point9]
    row_avg_9 = w1_09.mean(axis=1)
    refl9 = input("Specify column # representing spectral reflectance for point 9: ")
    refl9 = list(refl9)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl9 = [int(i) for i in refl9]       # This is list comprehension
    refl9_test = df.iloc[:, refl9]
    refl9_test_2 = refl9_test.mean(axis=1)
    point9_ndvi = (row_avg_9)/(refl9_test_2)
    
    # POINT 10
    w1_10_cols = input("Enter the column index numbers for sample point 10 (with a space between each column #): ")
    w1_10_cols = list(w1_10_cols.split())
    point10 = [int(i) for i in w1_10_cols]
    w1_10 = df.iloc[:, point10]
    row_avg_10 = w1_10.mean(axis=1)
    refl10 = input("Specify column # representing spectral reflectance for point 10: ")
    refl10 = list(refl10)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl10 = [int(i) for i in refl10]       # This is list comprehension
    refl10_test = df.iloc[:, refl10]
    refl10_test_2 = refl10_test.mean(axis=1)
    point10_ndvi = (row_avg_10)/(refl10_test_2)
    
    # POINT 11
    w1_11_cols = input("Enter the column index numbers for sample point 11 (with a space between each column #): ")
    w1_11_cols = list(w1_11_cols.split())
    point11 = [int(i) for i in w1_11_cols]
    w1_11 = df.iloc[:, point11]
    row_avg_11 = w1_11.mean(axis=1)
    refl11 = input("Specify column # representing spectral reflectance for point 11: ")
    refl11 = list(refl11)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl11 = [int(i) for i in refl11]       # This is list comprehension
    refl11_test = df.iloc[:, refl11]
    refl11_test_2 = refl11_test.mean(axis=1)
    point11_ndvi = (row_avg_11)/(refl11_test_2)
    
    # POINT 12
    w1_12_cols = input("Enter the column index numbers for sample point 12 (with a space between each column #): ")
    w1_12_cols = list(w1_12_cols.split())
    point12 = [int(i) for i in w1_12_cols]
    w1_12 = df.iloc[:, point12]
    row_avg_12 = w1_12.mean(axis=1)
    refl12 = input("Specify column # representing spectral reflectance for point 12: ")
    refl12 = list(refl12)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl12 = [int(i) for i in refl12]       # This is list comprehension
    refl12_test = df.iloc[:, refl12]
    refl12_test_2 = refl12_test.mean(axis=1)
    point12_ndvi = (row_avg_12)/(refl12_test_2)
    
    
    # POINT 13
    w1_13_cols = input("Enter the column index numbers for sample point 13 (with a space between each column #): ")
    w1_13_cols = list(w1_13_cols.split())
    point13 = [int(i) for i in w1_13_cols]
    w1_13 = df.iloc[:, point13]
    row_avg_13 = w1_13.mean(axis=1)
    refl13 = input("Specify column # representing spectral reflectance for point 13: ")
    refl13 = list(refl13)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl13 = [int(i) for i in refl13]       # This is list comprehension
    refl13_test = df.iloc[:, refl13]
    refl13_test_2 = refl13_test.mean(axis=1)
    point13_ndvi = (row_avg_13)/(refl13_test_2)
    
    # POINT 14
    w1_14_cols = input("Enter the column index numbers for sample point 14 (with a space between each column #): ")
    w1_14_cols = list(w1_14_cols.split())
    point14 = [int(i) for i in w1_14_cols]
    w1_14 = df.iloc[:, point14]
    row_avg_14 = w1_14.mean(axis=1)
    refl14 = input("Specify column # representing spectral reflectance for point 14: ")
    refl14 = list(refl14)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl14 = [int(i) for i in refl14]       # This is list comprehension
    refl14_test = df.iloc[:, refl14]
    refl14_test_2 = refl14_test.mean(axis=1)
    point14_ndvi = (row_avg_14)/(refl14_test_2)
    
    # POINT 15
    w1_15_cols = input("Enter the column index numbers for sample point 15 (with a space between each column #): ")
    w1_15_cols = list(w1_15_cols.split())
    point15 = [int(i) for i in w1_15_cols]
    w1_15 = df.iloc[:, point15]
    row_avg_15 = w1_15.mean(axis=1)
    refl15 = input("Specify column # representing spectral reflectance for point 15: ")
    refl15 = list(refl15)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl15 = [int(i) for i in refl15]       # This is list comprehension
    refl15_test = df.iloc[:, refl15]
    refl15_test_2 = refl15_test.mean(axis=1)
    point15_ndvi = (row_avg_15)/(refl15_test_2)
    
    # POINT 16
    w1_16_cols = input("Enter the column index numbers for sample point 16 (with a space between each column #): ")
    w1_16_cols = list(w1_16_cols.split())
    point16 = [int(i) for i in w1_16_cols]
    w1_16 = df.iloc[:, point16]
    row_avg_16 = w1_16.mean(axis=1)
    refl16 = input("Specify column # representing spectral reflectance for point 16: ")
    refl16 = list(refl16)
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    refl16 = [int(i) for i in refl16]       # This is list comprehension
    refl16_test = df.iloc[:, refl16]
    refl16_test_2 = refl16_test.mean(axis=1)
    point16_ndvi = (row_avg_16)/(refl16_test_2)
    
    # OUTPUT TO EXCEL FILE
    # https://stackoverflow.com/questions/13437727/writing-to-an-excel-spreadsheet
    excel_filename = input('Enter file name to save to (.xlsx): ')
    sheetName = input('Enter sheet name for .xlsx file: ')
    ndvi_df = pd.DataFrame({'NDVI Point 1': point1_ndvi, 'NDVI Point 2': point2_ndvi, 'NDVI Point 3': point3_ndvi, 'NDVI Point 4': point4_ndvi, 'NDVI Point 5': point5_ndvi, 'NDVI Point 6': point6_ndvi, 'NDVI Point 7': point7_ndvi, 'NDVI Point 8': point8_ndvi, 'NDVI Point 9': point9_ndvi, 'NDVI Point 10': point10_ndvi, 'NDVI Point 11': point11_ndvi, 'NDVI Point 12': point12_ndvi, 'NDVI Point 12': point12_ndvi, 'NDVI Point 13': point13_ndvi, 'NDVI Point 14': point14_ndvi, 'NDVI Point 15': point15_ndvi, 'NDVI Point 16': point16_ndvi})
    ndvi_df.to_excel(excel_filename, sheet_name= sheetName, index=False)
    
    file_path = os.path.dirname(os.path.realpath(excel_filename))
    print("Output NDVI file", excel_filename, " has been saved to: ", file_path)
    
