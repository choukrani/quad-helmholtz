#!/usr/bin/python3
#-*- coding: utf-8 -*-

import numpy as np
import copy  

import data

##----------------------------------
#  Methode des trapezes : 
def quadTrap(a,b,p,f):
    h = (b-a)/p
    res = 0.0
    x = a
    fx = f(x)
    while(x < b-1e-8):
        # Completer ICI : formule simplifiée
        fxPh = f(x+h)
        res +=2*fxPh 
        x = x + h
        fx = fxPh
    
    res = f(a)+f(b)+res
        
    return res*(h/2)
    
##----------------------------------


##----------------------------------
#  Methode des pt milieu : 
def quadHerm(a,b,p,f,df):
    h = (b-a)/p
    res = 0.0
    x = a
    eps = 1e-5
    while(x < b-1e-8):
        # Completer ICI :
        #fx1 = f(x)
        fx2 = f(x + (h/2)) 
        res += 2 * fx2 
                
        x = x + h
    
    dfa = df(a) 
    dfb = df(b) 
    
    # Completer ICI :
    res = res + (h/12)*(dfb - dfa)
    
    return res * (h/2)
##----------------------------------


##----------------------------------
#  Methode des Gauss : 
def quadGauss(a,b,p,f):
    h = (b-a)/p
    res = 0.0
    x = a
    c1=(-1+np.sqrt(3))/(2*np.sqrt(3))
    
    c2=(1+np.sqrt(3))/(2*np.sqrt(3))
  
    while(x < b-1e-8):
        # Completer ICI :
        fx1 =f(c1*h+x)
        fx2=f(c2*h+x)
        res += fx1+fx2
        
        x = x + h
        
    res = res * (h/2)
        
    return res 
##----------------------------------

