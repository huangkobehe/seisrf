# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 11:28:11 2021

@author: Lenovo
"""
import numpy as np;

def iasp91(r):
    global Iasprad,Iaspvp,Iaspvs,Iaspden,Iaspqk,Iaspqs
    readarrays='true ';

    
    Iasprad=np.matrix([[1217.1],
    [3482.0],
    [3631.0],
    [5611.0],
    [5711.0],
    [5961.0],
    [6161.0],
    [6251.0],
    [6336.0],
    [6351.0],
    [6371.0]]);
    
    Iaspvp =np.matrix([[11.24094,   0.     ,  -4.09689,   0.   ],
    [10.03904,   3.75665, -13.67046,   0.    ], 
    [14.49470,  -1.47089,   0.     ,   0.    ],
    [25.14860, -41.15380,  51.99320, -26.6083],
    [25.96984, -16.93412,   0.     ,   0.    ],
    [29.38896, -21.40656,   0.     ,   0.    ],
    [30.78765, -23.25415,   0.     ,   0.    ],
    [25.41389, -17.69722,   0.     ,   0.    ],
    [ 8.78541,  -0.74953,   0.     ,   0.    ],
    [ 6.5    ,   0.     ,   0.     ,   0.    ],
    [ 5.8    ,   0.     ,   0.     ,   0.    ]]);
    
    Iaspvs =np.matrix([[3.56454,   0.     ,  -3.45241,   0.    ],
    [0.     ,   0.     ,   0.     ,   0.    ],
    [8.16616,  -1.58206,   0.     ,   0.    ],
    [12.93030, -21.25900,  27.89880, -14.1080],
    [20.76890, -16.53147,   0.     ,   0.    ],
    [17.70732, -13.50652,   0.     ,   0.    ],
    [15.24213, -11.08552,   0.     ,   0.    ],
    [5.75020,  -1.27420,   0.     ,   0.    ],
    [6.706231, -2.248585,  0.     ,   0.    ],
    [3.75   ,   0.     ,   0.     ,   0.    ],
    [3.36   ,   0.     ,   0.     ,   0.    ]]);
    
    Iaspden=np.matrix([[13.01219,   0.     ,  -8.45115,   0.],    
    [12.58405,  -1.69822,  -1.94472,  -7.10867],
    [7.18300,  -2.98500,   0.     ,   0.],
    [6.81848,  -1.68035,  -1.16066,  -0.01144],
    [7.75231,  -3.77163,   0.     ,   0.],
    [11.12044,  -7.87128,   0.     ,   0.],
    [7.15937,  -3.86083,   0.     ,   0.],
    [7.15661,  -3.85799,   0.     ,   0.],
    [7.15122,  -3.85258,   0.     ,   0.],
    [2.92000,   0.00000,   0.     ,   0.],
    [2.72000,   0.00000,   0.     ,   0.     ]]);
    
    Iaspqk=np.matrix([[1327.7],
    [57823.0],
    [57823.0],
    [57823.0],
    [57823.0],
    [57823.0],
    [57823.0],
    [57823.0],
    [57823.0],
    [57823.0],
    [57823.0]]);
    
    Iaspqs=np.matrix([[84.6],
    [9.e99],
    [312.0],
    [312.0],
    [312.0],
    [143.0],
    [143.0],
    [ 80.0],
    [600.0],
    [600.0],
    [600.0]]);

    radius=6371;
    pvel=np.zeros(np.size(r));svel=pvel;
    density=pvel; qk=pvel;qs=pvel;
    if ('Iaspvp'):
        if len(Iaspvp) == 11:
            if Iaspvp[3,3] == -26.6083:
                readarrays='false'
    if readarrays == 'true':
        print('reading in arrays')
    
    # for j in range(1,r+1):
    #    if r[j] <= 0:
    #      pvel[j]=Iaspvp[0,0];      svel[j]=Iaspvs[0,0]; 
    #      density[j]=Iaspden[0,0];  qk[j]=Iaspqk[0];      qs[j]=Iaspqs[0];
    #    elif r[j] >= radius:
    #      pvel[j]=Iaspvp[10,0];     svel[j]=Iaspvs[10,0];
    #      density[j]=Iaspden[10,0]; qk[j]=Iaspqk[10];     qs[j]=Iaspqs[10];
    #    else:
    # i=min( jg for jg in range(len(Iasprad)) if Iasprad[jg]>r[j] );
    # y=r[j]/radius;
    # x=np.array([[0],[y],[y*y],[y*y*y]]);
    # pvel[j]=Iaspvp[i,:]*x;
    # svel[j]=Iaspvs[i,:]*x;
    # density[j]=Iaspden[i,:]*x;
    # qk[j]=Iaspqk[i];
    # qs[j]=Iaspqs[i];
   
    
    i=min( jg for jg in range(len(Iasprad)) if Iasprad[jg]>r );
    y=r/radius;
    x=np.array([[1],[y],[y*y],[y*y*y]]);
    # aa=Iaspvp[i,:]
    # pvel = ( aa for aa in range(len(Iaspvp[i,:])) Iaspvp[i,aa] )
    pvel=Iaspvp[i,:]*x;
    svel=Iaspvs[i,:]*x;
    density=Iaspden[i,:]*x;
    qk=Iaspqk[i];
    qs=Iaspqs[i];
    
    
    vratio=svel/pvel;b=(4/3)*(vratio*vratio);
    temp1=1/((1+b)*qk);
    temp2=b/qs;
    qp=1./(temp1+temp2);

    return pvel,svel,density,qp,qs,qk






