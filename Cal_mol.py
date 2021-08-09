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



for depth_value in range(300,800,10):
    print(depth_value)
    for jj in range(1,j):
        for kk in range(1,k):
            for hh in range(1,h):
                if data_dep[jj] == depth_value:
                    print(jj,kk,hh)
                    if (data_vpv[jj,kk,hh] != 99999 or data_vph[jj,kk,hh]!= 99999 or data_vsv[jj,kk,hh] != 99999 or data_vsh[jj,kk,hh] != 99999):
                        x_axias = data_lon[hh]
                        y_axias = data_lat[kk]
                        z_axias = data_dep[jj]
                        Vpv = data_vpv[jj,kk,hh]
                        Vph = data_vph[jj,kk,hh]
                        Vsv = data_vsv[jj,kk,hh]
                        Vsh = data_vsh[jj,kk,hh]
                        Vp =(((Vpv ** 2) + 4*(Vph ** 2))/5) ** 0.5
                        Vs =((2*(Vsv ** 2) + (Vsh ** 2))/3) ** 0.5
                        print(x_axias,y_axias,z_axias,Vp,Vs)
                        model_fil = 'FWEA18-' + str(depth_value) + '.txt'
                        with open(model_fil,mode='a',encoding='UTF-8') as f:
                            f.write("%f %f %f %f %f \n" % (x_axias,y_axias,z_axias,Vp,Vs))
                          
 
    data = open(model_fil)  
    lon_p = []
    lat_p = []
    dep_p = []
    Vp_p = []
    Vs_p = []
    for row in data.readlines(): 
          row=row.split(" ")
          lon_p.append(float(row[0]))
          lat_p.append(float(row[1]))
          dep_p.append(float(row[2]))
          Vp_p.append(float(row[3]))
          Vs_p.append(float(row[4]))
    
    #开始画图                   
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(min(data_lon[:]),max(data_lon),min(data_lat),max(data_lat))
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    picnam = depth_value
    fig = pygmt.Figure()
    
    
    # pygmt.blockmean(
    #             x = lon_p,
    #             y = lat_p,
    #             z = Vp_p,
    #             spacing = "0.25/0.25",
    #             region = [min(lon_p),max(lon_p),min(lat_p),max(lat_p)],
    #             outfile = "C:\\Users\\Lenovo\\Desktop\\CN_model\\mygrid.txt", 
    #             )
    
    
    pygmt.surface(
                # data = "C:\\Users\\Lenovo\\Desktop\\CN_model\\mygrid.txt",
                x = lon_p,
                y = lat_p,
                z = Vp_p,
                region = [min(lon_p),max(lon_p),min(lat_p),max(lat_p)],
                outfile = "C:\\Users\\Lenovo\\Desktop\\cal_model\\mygrid.nc",
                spacing = "0.25/0.25",
                )
    
    
    
    # pygmt.xyz2grd(
    #             # data = "C:\\Users\\Lenovo\\Desktop\\CN_model\\mygrid.txt",
    #             x = lon_p,
    #             y = lat_p,
    #             z = Vp_p,
    #             region = [min(lon_p),max(lon_p),min(lat_p),max(lat_p)],
    #             outfile = "C:\\Users\\Lenovo\\Desktop\\CN_model\\mygrid.nc",
    #             spacing = "0.25/0.25",
    #             )
    
    pygmt.makecpt(
                cmap="jet", color_model="-r", series=(min(Vp_p), max(Vp_p)),output ="my.cpt",reverse=True
                )
    
    fig.grdimage(
                region = [min(lon_p),max(lon_p),min(lat_p),max(lat_p)],
                grid = "mygrid.nc",
                projection = "T120/12c", 
                cmap = "my.cpt",
                )
    
    fig.coast(
                region = [min(data_lon),max(data_lon),min(data_lat),max(data_lat)],
                borders = ["1/0.5p,black", "2/0.5p,red", "3/0.5p,blue"],
                projection = "T120/12c",
                # land = "grey",
                # water = "lightblue",
                shorelines = True,
                frame = "ag5" 
                )
    
    fig.text(
        region = [min(lon_p),max(lon_p),min(lat_p),max(lat_p)],
        projection = "T120/12c", 
        text=[str(depth_value) + "km"], x=[145], y=[15],font="10p,Helvetica-Bold,black"
        )
    #fig.colorbar(frame=["a", "x+lVelocity", "y+lkm/s"])
                
    fig.show()
    fig.savefig('C:\\Users\\Lenovo\\Desktop\\cal_model\\model-' + str(depth_value)+".png",dpi=600)
 