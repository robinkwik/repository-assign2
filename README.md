# NDVI
Automated calculation of NDVI from an excel file.

In this repository I have uploaded the original version of the NDVI calculation file (RAW) as well as more refined version.


ndvi_calculation_pandas_RAW.py represents my first attempt at coding to calculate NDVI from an EXCEL file where the spectral reflectance has already been calculated by the user. 
ndvi_calculation_as_function.py represents ndvi_calculation_pandas_RAW.py as a blackbox definition function.


reflectance_calculation_from_RAW_DATA.py represents the calculation of SPECTRAL REFLECTANCE from RAW DN values in an Excel File (.csv) (ViewSpecPro --> ASCII Export --> TXT File --> EXCEL File (.csv)). This presents a more useful tool for SPECTRAL REFLECTANCE calculation and saves much more time.
ASD-Calc-SpecRefl-Function.py represents a function produced from ndvi_reflectance_calculation_from_RAW_DATA.py. Represents a more organized version, however need to add exceptions.

Paul_20200527.csv can be used as a test document.
