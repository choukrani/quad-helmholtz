#!/usr/bin/python3
#-*- coding: utf-8 -*-

import numpy as np
import copy
  

##----------------------------------
#  fonction f a integrer :
def f(x):
    # Parametre k :
    kk = 1.0
    ## Fonction cos :
    # Completer ICI :
    res = np.cos(2 * kk * np.pi * x)
    
    # Autre fonction de votre choix :
    #res= np.cos(x)/(x+0.5)
    #res= np.cos(70*x)/(x+1)
    #res=np.sqrt(x)*np.sin(1/x)
    return res
##---------------------------------- 


##----------------------------------
#  derivee df de la fonction f :
def df(x):
    # Parametre k :
    kk = 1.0
    # Fonction cos' :
    # Completer ICI :
    res = -2*kk*np.pi*np.sin(2*kk*np.pi*x)
    #res=- ( (x+0.5)*sin(x)+cos(x)  / (x+0.5)*(x+0.5) )
    #res=- (70*(x+1)*np.sin(70*x)+np.cos(70*x))/(x+1)*(x+1)
    #res=(x*np.sin(1/x)-2*np.cos(1/x))/(2*x**(3/2))
    return res
##----------------------------------  


