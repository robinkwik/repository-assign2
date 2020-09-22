# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:15:35 2020

@author: robin
"""
import pandas as pd
import os

fileName = input("Please enter ASD file name (.csv format)")

# Test filename = 'Paul_20200527.csv'

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
    
sp = int(input("Enter number of sample points: "))
sp_range = range(1, sp+1, 1)
sp_list = []
for num in sp_range:
    sp_list.append(num)
print("Sample points:", sp_list)

sample_cols = []
count = 0

# for value in sp_list:
    # sample_cols[value] = input(f"Enter the column index numbers for sample point {value} (with a space between each column #): ")

dict = {} #Empty dictionary to add values into

for i in sp_list:
    dict[i] = input(f"Enter column numbers for sample point {i}: ")
print("column numbers for each sample point: ", dict)
