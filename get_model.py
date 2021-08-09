# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 20:47:58 2021

@author: Lenovo
"""

import netCDF4
import matplotlib.pyplot as plt
import numpy as np
import cmath
import pygmt
from netCDF4 import Dataset
from numpy import *
from scipy.interpolate import griddata
nc_obj = Dataset('C:\\Users\\Lenovo\\Desktop\\cal_model\\FWEA18_kmps.nc')

Dep = (nc_obj.variables['depth'][:])
Lon = (nc_obj.variables['longitude'][:])
Lat = (nc_obj.variables['latitude'][:])
Vsh = (nc_obj.variables['vsh'][:])
Vsv = (nc_obj.variables['vsv'][:])
Vph = (nc_obj.variables['vph'][:])
Vpv = (nc_obj.variables['vpv'][:])

data_dep = np.array(Dep)
data_lat = np.array(Lat)
data_lon = np.array(Lon)
data_vsh = np.array(Vsh)
data_vsv = np.array(Vsv)
data_vph = np.array(Vph)
data_vpv = np.array(Vpv)

j=len(data_dep)
k=len(data_lat)
h=len(data_lon)
lat=np.arange(17,56,79)


grdnum=1

for lat in np.linspace(17,55,77):
   for lon in np.linspace(73,136,127):
        print(lon,lat);
        grdnum=grdnum+1;
   
model_fil = 'C:\\Users\\Lenovo\\Desktop\\cal_model\\get_model\\model_FWEA18_smooth_noheading.grid.lst'                     
data = open(model_fil)  
lon_p = []
lat_p = []
dep_p = []
Vp_per_p = []
Vs_per_p = []
Vp_0_p = [] 
Vs_0_p = []
for row in data.readlines(): 
      #row=row.split("    ")
      lon_p.append(float(row[0]))
      lat_p.append(float(row[1]))
      dep_p.append(float(row[2]))
      Vp_per_p.append(float(row[15]))
      Vs_per_p.append(float(row[16]))   
      Vp_0_p.append(float(row[17]))
      Vs_0_p.append(float(row[18]))
                        
                        
                        
        