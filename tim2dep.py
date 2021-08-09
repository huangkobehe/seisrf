# -*- coding: utf-8 -*-

#Created on Sat Aug  7 11:28:11 2021

#@author: Lenovo

import numpy as np
from iasp91 import iasp91
import math
def tim2dep(rayP,tim,model):
    ER = 6371;
    pp=rayP/111.19;
    za=0;
    zz=0;
    t=0;th=0;xp=0;xs=0;
    xxs=0;xxp=0;pdst=0;
    h = [];dep = [];vp = [];vs = [];ro = [];pvp = []
    for i in range(1,801):
        [pvel,svel,density,qp,qs,qk] = iasp91(ER-i);
        z1k=zz+1*0.5;
        zz=zz+1;
        y1=ER/(ER-z1k);
        yz=ER/(ER-zz);
        zm=ER*math.log(yz);
        h_va=zm-za
        #h.append(zm-za);
        #dep.append(i);
        za=zm;
        #vp.append(pvel*y1);
        #vs.append(svel*y1);
        #ro.append(density/y1);
        #print(h_va)
        #pvp.append(pp*pvel*y1);
        if pp*pvel*y1>=1:
            pvp=0.9999
        xp=(h_va)*(math.tan(math.asin(pp*pvel*y1)));
        xs=(h_va)*(math.tan(math.asin(pp*svel*y1)));
        xxp=xxp+xp/y1;xxs=xxs+xs/y1;
        pdst=pdst+(xs/(h_va))/(ER-i)*180/(math.pi);
        t=t+(h_va)/(math.cos(math.asin(pp*svel*y1))*svel*y1)-(h_va)/(math.cos(math.asin(pp*pvel*y1))*(pvel*y1))+(xp-xs)*pp;
        if t>=tim:
            dep=i;
            break

    return dep;