# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 22:57:03 2021

@author: Lenovo
"""
#import pygmt
import netCDF4
import matplotlib.pyplot as plt
import numpy as np
import cmath
import pygmt
from netCDF4 import Dataset
from numpy import *
from scipy.interpolate import griddata
nc_obj = Dataset('C:\\Users\\Lenovo\\Desktop\\cal_model\\FWEA18_kmps.nc')

print(nc_obj)

print('_________________________')
print(nc_obj.variables.keys())
print('_________________________')

for i in nc_obj.variables.keys():
    print('+++++++++++++++++++++++++')
    print(i)
    print(nc_obj.variables[i])
    
    
def find_max(data_matrix):
	new_data = []
	for i in range(len(data_matrix)):
		new_data.append(max(data_matrix[i]))
	print("data_matrix最大值为",max(new_data))
    
def find_min(data_matrix):
	new_data = []
	for i in range(len(data_matrix)):
		new_data.append(min(data_matrix[i]))
	print("data_matrix最小值为",min(new_data))
    
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
print("_____________________________________________")



# for i in range(1,3923721,81):
#     print(i)
#     print('Opsssssssssssssssssssssssss')
#     while (i<=i+80):
#         print(i)
#         i=i+1



for lat in np.linspace(17,55,77):
    for lon in np.linspace(73,136,127):
        index=0
        Vs= [];Vp= [];Vp_r= [];Vs_r= [];Vp_l= [];Vs_l= [];Vp_u= [];Vs_u= [];Vp_b= [];Vs_b= [];
        for kk in range(0,k):    #LOOP FOR LATTITUDE
            for hh in range(0,h):    #LOOP FOR LONGITUDE
                for jj in range(0,j):    #LOOP FOR DEPTH
                    if (lat-0.25 == data_lat[kk]) and (lon == data_lon[hh]):
                        index=index+1
                        print("This is point is in the bottom corner.")
                        if (data_vpv[jj,kk,hh] != 99999 or data_vph[jj,kk,hh]!= 99999 or data_vsv[jj,kk,hh] != 99999 or data_vsh[jj,kk,hh] != 99999):
                            Vpv_b = data_vpv[jj,kk,hh]
                            Vph_b = data_vph[jj,kk,hh]
                            Vsv_b = data_vsv[jj,kk,hh]
                            Vsh_b = data_vsh[jj,kk,hh]
                            Vp_b.append((((Vpv_b ** 2) + 4*(Vph_b ** 2))/5) ** 0.5)
                            Vs_b.append(((2*(Vsv_b ** 2) + (Vsh_b ** 2))/3) ** 0.5)
                    elif (lat+0.25 == data_lat[kk]) and (lon == data_lon[hh]):
                        index=index+1
                        print("This is point is in the upper corner.")
                        if (data_vpv[jj,kk,hh] != 99999 or data_vph[jj,kk,hh]!= 99999 or data_vsv[jj,kk,hh] != 99999 or data_vsh[jj,kk,hh] != 99999):
                            Vpv_u = data_vpv[jj,kk,hh]
                            Vph_u = data_vph[jj,kk,hh]
                            Vsv_u = data_vsv[jj,kk,hh]
                            Vsh_u = data_vsh[jj,kk,hh]
                            Vp_u.append((((Vpv_u ** 2) + 4*(Vph_u ** 2))/5) ** 0.5)
                            Vs_u.append(((2*(Vsv_u ** 2) + (Vsh_u ** 2))/3) ** 0.5)
                    elif (lat == data_lat[kk]) and (lon-0.25 == data_lon[hh]):
                        index=index+1
                        print("This is point is in the left corner.")
                        if (data_vpv[jj,kk,hh] != 99999 or data_vph[jj,kk,hh]!= 99999 or data_vsv[jj,kk,hh] != 99999 or data_vsh[jj,kk,hh] != 99999):
                            Vpv_l = data_vpv[jj,kk,hh]
                            Vph_l = data_vph[jj,kk,hh]
                            Vsv_l = data_vsv[jj,kk,hh]
                            Vsh_l = data_vsh[jj,kk,hh]
                            Vp_l.append((((Vpv_l ** 2) + 4*(Vph_l ** 2))/5) ** 0.5)
                            Vs_l.append(((2*(Vsv_l ** 2) + (Vsh_l ** 2))/3) ** 0.5)
                    elif (lat == data_lat[kk]) and (lon+0.25 == data_lon[hh]):
                        index=index+1
                        print("This is point is in the right corner.")
                        if (data_vpv[jj,kk,hh] != 99999 or data_vph[jj,kk,hh]!= 99999 or data_vsv[jj,kk,hh] != 99999 or data_vsh[jj,kk,hh] != 99999):
                            Vpv_r = data_vpv[jj,kk,hh]
                            Vph_r = data_vph[jj,kk,hh]
                            Vsv_r = data_vsv[jj,kk,hh]
                            Vsh_r = data_vsh[jj,kk,hh]
                            Vp_r.append((((Vpv_r ** 2) + 4*(Vph_r ** 2))/5) ** 0.5)
                            Vs_r.append(((2*(Vsv_r ** 2) + (Vsh_r ** 2))/3) ** 0.5)
        print("Bfore the witing index is ",index)
        if index == 4*81:
            
            for jj in range(0,j):
                Vs=((Vs_r[jj]+Vs_l[jj]+Vs_u[jj]+Vs_b[jj])/4);
                Vp=((Vp_r[jj]+Vp_l[jj]+Vp_u[jj]+Vp_b[jj])/4);  
                print(lon,lat,jj*10,Vp,Vs)
                model_fil = str(lat) + '_' + str(lon) + '.txt'
                if Vp != 0 and Vs != 0 :
                    print(Vp);print(Vs);print(jj)
                    with open(model_fil,mode='a',encoding='UTF-8') as f:
                        f.write("%f %f %f %f %f \n" % (lon,lat,jj,Vp,Vs))
            del Vp_r;Vs_r;Vp_l;Vs_l;Vp_u;Vs_u;Vp_b;Vs_b;Vs;Vp
            continue;
        # jl=1
        # if type(Vp_r) == list:
        #     Vp_r = 0
        #     jl=jl+1
        # if type(Vp_l) == list:
        #     Vp_l = 0
        #     jl=jl+1
        # if type(Vp_u) == list:
        #     Vp_u = 0
        #     jl=jl+1         
        # if type(Vp_b) == list:
        #     Vp_b = 0
        #     jl=jl+1
        # Vp=(Vp_r+Vp_l+Vp_u+Vp_b);Vp = Vp/4;
    
        # jk=1                                    
        # if type(Vs_r) == list:
        #     Vs_r = 0
        #     jk=jk+1
        # if type(Vs_l) == list:
        #     Vs_l = 0
        #     jk=jk+1
        # if type(Vs_u) == list:
        #     Vs_u = 0
        #     jk=jk+1
        # if type(Vs_b) == list:
        #     Vs_b = 0
        #     jk=jk+1
        
        # for jj in range(1,j):
        #     Vs[jj].append((Vs_r[jj]+Vs_l[jj]+Vs_u[jj]+Vs_b[jj])/4);
        #     Vp[jj].append((Vp_r[jj]+Vp_l[jj]+Vp_u[jj]+Vp_b[jj])/4);   
        #     if Vs[jj]!=0 and Vp[jj]!=0:
        #         print(lon,lat,jj*10,Vp[jj],Vs[jj])
        #     model_fil = str(lat) + '_' + str(lon) + '.txt'
        #     if Vp[jj] != 0 and Vs[jj] != 0 :
        #         print(Vp[jj]);print(Vs[jj])
        #         with open(model_fil,mode='a',encoding='UTF-8') as f:
        #             f.write("%f %f %f %f %f \n" % (lon,lat,jj,Vp[jj],Vs[jj]))
  
      
                            # Vp=(Vp_r+Vp_l+Vp_u+Vp_b);Vp = Vp/4 
                    #         # Vs=(Vs_r+Vs_l+Vs_u+Vs_b);Vs = Vs/4  
                    # elif (Vp_r) or (Vp_l) or (Vp_u) or (Vp_b):
                    #     # print("mmmmmmmmmmmmmmmmmmmmmmmm")
                    #     print(Vp,Vs)
                        

    
    # for jj in range(1,j):
    #     for kk in range(1,k):
    #         for hh in range(1,h):
    #             #if data_dep[jj] == depth_value:
    #                 print(jj,kk,hh)
    #                 if (data_vpv[jj,kk,hh] != 99999 or data_vph[jj,kk,hh]!= 99999 or data_vsv[jj,kk,hh] != 99999 or data_vsh[jj,kk,hh] != 99999):
    #                     x_axias = data_lon[hh]
    #                     y_axias = data_lat[kk]
    #                     z_axias = data_dep[jj]
    #                     Vpv = data_vpv[jj,kk,hh]
    #                     Vph = data_vph[jj,kk,hh]
    #                     Vsv = data_vsv[jj,kk,hh]
    #                     Vsh = data_vsh[jj,kk,hh]
    #                     Vp =(((Vpv ** 2) + 4*(Vph ** 2))/5) ** 0.5
    #                     Vs =((2*(Vsv ** 2) + (Vsh ** 2))/3) ** 0.5
    #                     print(x_axias,y_axias,z_axias,Vp,Vs)
    #                     model_fil = 'FWEA18-' + str(depth_value) + '.txt'
    #                     with open(model_fil,mode='a',encoding='UTF-8') as f:
    #                         f.write("%f %f %f %f %f \n" % (x_axias,y_axias,z_axias,Vp,Vs))
