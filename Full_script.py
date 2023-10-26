# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 19:54:35 2023

@author: iyanu
"""

import arcpy
import os 
##Extract Daytime raster from Aqua Folder 

arcpy.env.workspace = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua/'
os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/')
rootPath = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua/'
outputPath = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'

hdfList = arcpy.ListRasters()

for filename in hdfList:
    arcpy.ExtractSubDataset_management(in_raster= rootPath + filename, out_raster= outputPath + filename[8:-29] + ".tif", subdataset_index= "0" )

##Extract Nightime Rasters from Aqua Folder
os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/')
outputPath = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'

for filename in hdfList:
    arcpy.ExtractSubDataset_management(in_raster= rootPath + filename, out_raster= outputPath + filename[8:-29] + ".tif", subdataset_index= "4" )
 
##Extract Daytime Raster from Terra Folder 
arcpy.env.workspace = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Terra/'
os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_D/')
rootPath = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Terra/'
outputPath = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_D/'

hdfList = arcpy.ListRasters()

for filename in hdfList:
    arcpy.ExtractSubDataset_management(in_raster= rootPath + filename, out_raster= outputPath + filename[8:-29] + ".tif", subdataset_index= "0" )

##Extract Nightime Rasters from Terra Folder
os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_N/')
outputPath = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_N/'

for filename in hdfList:
    arcpy.ExtractSubDataset_management(in_raster= rootPath + filename, out_raster= outputPath + filename[8:-29] + ".tif", subdataset_index= "4" )


##Create Mean for Day and Nighttime temperatures for AQUA

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("*", "TIF")
os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_mean/')

from arcpy.sa import *
for (i,j) in zip(Aqua_D, Aqua_N):
    outCellStats =CellStatistics([f'C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/{i}',f'C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/{j}'], "MEAN", "NODATA")
    outCellStats.save(f"C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_mean/{i}")
        
##Create Mean for Day and Nighttime temperatures for Terra

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_D/'
Terra_D = arcpy.ListRasters("*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_N/'
Terra_N = arcpy.ListRasters("*", "TIF")
os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_mean/')

from arcpy.sa import *
for (i,j) in zip(Terra_D,Terra_N):
    outCellStats =CellStatistics([f'C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_D/{i}',f'C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_N/{j}'], "MEAN", "NODATA")
    outCellStats.save(f"C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_mean/{i}")
    
        
##Create Mean for Daily Land Surface Temperature Of all four Rasters 

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_D/'
Terra_D = arcpy.ListRasters("*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_N/'
Terra_N = arcpy.ListRasters("*", "TIF")

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("*", "TIF")


os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Daily_Mean/')


from arcpy.sa import *
for (i,j,k,l) in zip(Terra_D,Terra_N,Aqua_D, Aqua_N):
    outCellStats =CellStatistics([f'C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_D/{i}',f'C:/Users/iyanu/OneDrive/Desktop/Resit/Terra_N/{j}', f'C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/{k}', f'C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/{l}' ], "MEAN", "NODATA")
    outCellStats.save(f"C:/Users/iyanu/OneDrive/Desktop/Resit/Daily_Mean/{i}")
    
#Apply Scale Factor

arcpy.env.workspace = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Daily_Mean/'

rootPath = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Daily_Mean/'

os.mkdir( 'C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_K/')


outputPath = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_K/'

rasterList = arcpy.ListRasters("*", "TIF")

for filename in rasterList:
     output_raster = arcpy.sa.Raster(filename) * 0.02
     output_raster.save(outputPath + filename) 
     

##Convert to Degrees Celcius

arcpy.env.workspace = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_K/'

rootPath = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_K/'

os.mkdir( 'C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_C/')

outputPath = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_C/'

rasterList = arcpy.ListRasters("*", "TIF")

for filename in rasterList:
     output_raster = arcpy.sa.Raster(filename) - 273.15     
     output_raster.save(outputPath + filename)
     
##Mean For 2019 

##Create Mean for Daily Land Surface Temperature for 2019 only and apply sclae factor 

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Terra_D = arcpy.ListRasters("A2019*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Terra_N = arcpy.ListRasters("A2019*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_2019/')

Output = CellStatistics([Aqua_D, Aqua_N] , "MEAN", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_2019/Mean2019.tif')


filename = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_2019/Mean2019.tif'

output_raster = arcpy.sa.Raster(filename) * 0.02

output_raster.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_2019/Mean2019_K.tif')


##Create Mean for Daily Land Surface Temperature for 2020 only and apply sclae factor 

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Terra_D = arcpy.ListRasters("A2020*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Terra_N = arcpy.ListRasters("A2020*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_2020/')

Output = CellStatistics([Aqua_D, Aqua_N] , "MEAN", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_2020/Mean2020.tif')


filename = 'C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_2020/Mean2020.tif'

output_raster = arcpy.sa.Raster(filename) * 0.02

output_raster.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Mean_2020/Mean2020_K.tif')

##Median For 2019

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("A2019*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("A2019*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Median_2019/')

Output = CellStatistics([Aqua_D, Aqua_N] , "MEAN", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Median_2019/Median2019.tif')

##Median for 2020

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("A2020*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("A2020*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Median_2020/')

Output = CellStatistics([Aqua_D, Aqua_N] , "MEDIAN", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Median_2020/Median2020.tif')

##Majority For 2019

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("A2019*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("A2019*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Majority_2019/')


Output = CellStatistics([Aqua_D, Aqua_N] , "MAJORITY", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Majority_2019/Majority2019.tif')

##Majority for 2020 

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("A2020*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("A2020*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Majority_2020/')

Output = CellStatistics([Aqua_D, Aqua_N] , "MAJORITY", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Majority_2020/Majority2020.tif')

##Minimum for 2019

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("A2019*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("A2019*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Minimum_2019/')


Output = CellStatistics([Aqua_D, Aqua_N] , "MINIMUM", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Minimum_2019/Minimum2019.tif')

##Minimum for 2020 

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("A2020*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("A2020*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Minimum_2020/')

Output = CellStatistics([Aqua_D, Aqua_N] , "MINIMUM", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Minimum_2020/Minimum2020.tif')


##Percentile for 2019

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("A2019*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("A2019*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Percentile_2019/')


Output = CellStatistics([Aqua_D, Aqua_N] , "PERCENTILE", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Percentile_2019/Percentile2019.tif')

##Percentile for 2020 

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("A2020*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("A2020*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Percentile_2020/')

Output = CellStatistics([Aqua_D, Aqua_N] , "PERCENTILE", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Percentile_2020/Percentile2020.tif')

##Range for 2019

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("A2019*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("A2019*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Range_2019/')


Output = CellStatistics([Aqua_D, Aqua_N] , "RANGE", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Range_2019/Range2019.tif')

##Range for 2020 

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("A2020*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("A2020*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Range_2020/')

Output = CellStatistics([Aqua_D, Aqua_N] , "RANGE", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Range_2020/Range2020.tif')

##Standard deviation for 2019

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("A2019*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("A2019*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Standarddeviation_2019/')


Output = CellStatistics([Aqua_D, Aqua_N] , "STD", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Standarddeviation_2019/Standarddeviation2019.tif')

##Standard Deviation for 2020 

arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_D/'
Aqua_D = arcpy.ListRasters("A2020*", "TIF")
arcpy.env.workspace ='C:/Users/iyanu/OneDrive/Desktop/Resit/Aqua_N/'
Aqua_N = arcpy.ListRasters("A2020*", "TIF")

os.mkdir('C:/Users/iyanu/OneDrive/Desktop/Resit/Standarddeviation_2020/')

Output = CellStatistics([Aqua_D, Aqua_N] , "STD", "DATA")

Output.save('C:/Users/iyanu/OneDrive/Desktop/Resit/Standarddeviation_2020/Standarddeviation2020.tif')
