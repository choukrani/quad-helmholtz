#!/usr/bin/python3
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import affichage
import math
import cmath


import algo
import data


"""
    Quadrature et équation des ondes 
"""

##----------------------------------
# But du programme :
# 1. Test quadrature simple.
# 2. Analyse de convergence.
# 3. Résolution de l'équation d'Helmholtz.
butPrgm = 1
choix = 1
print("Que souhaitez vous faire ?")
print(" 1. Test quadrature simple.")
print(" 2. Analyse de convergence.")
print(" 3. Resolution Helmholtz.")
butPrgm = input("Entrer le choix : ")

print("")

# Choix de la methode de quadrature  :
print("Choix de la méthode de quadrature ?")
print(" 1. Trapèze.")
print(" 2. Gauss.")
print(" 3. Hermite.")
choixQuad = input("Entrer le choix : ")
print("")

##----------------------------------



##----------------------------------
# I. Test Interpolation d'une fonction f :
if (butPrgm=="1"):
    # Intervalle d'intégration
    # Modifier ICI :
    a=0
    b=0.75
    
    # p-sous intervalles pour la formule de quadrature (composite) :
    # Modifier ICI :
    p = 20
    
    resQuad = 0.0
    if (choixQuad == "1"):
        resQuad = algo.quadTrap(a,b,p,data.f)
    if (choixQuad == "2"):
        resQuad = algo.quadGauss(a,b,p,data.f)
    if (choixQuad == "3"):
        resQuad = algo.quadHerm(a,b,p,data.f,data.df)
         
    print("Calcul integrale de f : ",resQuad)  
     
    # Illustration formule de quadrature :
    if(p <= 20):
        affichage.afficherQuad(a,b,p,data.f,choixQuad)   
    else:
        print("Trop d'intervalle pour être représenté.")
##----------------------------------

##----------------------------------
# II. Analyse de convergence :
if (butPrgm=="2"):
    
    # Intervalle d'intégration
    # Modifier ICI :
    a=0.0
    b=0.75
    
    # parametre d'oscillation kk
    # Modifier ICI :
    kk = 1.0
    
    ## Integral exacte (pour f(x) = cos(2k pi x), attention penser a modifier dans data !)
    valEx = 0.0
    # Completer ICI :
    valEx = -(1/(2*np.pi))
    #valEx=0.437672
    # p-sous intervalle pour la formule de quadrature :
    list_p = [4,8,16,32,64,128]
    
    list_err = []
    list_res = []
    for p in list_p:
    
        resQuad = 0.0
        if (choixQuad == "1"):
            resQuad = algo.quadTrap(a,b,p,data.f)
        if (choixQuad == "2"):
            resQuad = algo.quadGauss(a,b,p,data.f)
        if (choixQuad == "3"):
            resQuad = algo.quadHerm(a,b,p,data.f,data.df) 
            
        list_res.append(resQuad)    
        list_err.append(np.abs(resQuad-valEx))
    
        
    ## Tracer courbe erreur :
    poly = np.polyfit(np.log10(list_p),np.log10(list_err),1)
    print("")
    print("Droite approchée : y=",poly[0],"x - ",np.abs(poly[1]))
    
    affichage.afficherConv([np.log10(list_p)],[np.log10(list_err)])
##----------------------------------



##----------------------------------
# III. Resolution Helmholtz :
if (butPrgm=="3"):
    
    # Choix 1 ou 2 pts  :
    print("Choix du nombre de source ponctuelle: ")
    print(" 1. 1 point.")
    print(" 2. 2 points.")
    choix = input("Entrer le choix : ")
    print("")

    if (choix=="1"):

        # Point (x,y) où on évalue la fonction u
        dx = 0.01
        dy = 0.01
        listX = np.arange(dx,5+dx*0.5,dx)
        listY = np.arange(-2.5,2.5+dy*0.5,dy)
        
        # Frequence ww et attenuation eps
        # Modifier ICI:
        ww = 20
        eps = 1.0j
        y0 = 0.0;
        
        p = 100
        res = np.zeros((len(listX),len(listY)),dtype=complex)
        for ix,x in enumerate(listX):
            resy = []
            # Completer ICI :
            myf = lambda xi : np.exp(-1.0j*xi*(listY - y0)) * np.exp(1.0j * cmath.sqrt(ww**2 + 1.0j * eps - xi**2) * x)
            mydf = lambda xi : ( (-1.0j*listY - (1.0j*xi*x)) / cmath.sqrt(ww**2 + 1.0j*eps - xi**2) ) * myf(xi)
            

            # Modifier ICI :
            a = -30.0
            b = 30.0
            resQuad = 0.0
            if (choixQuad == "1"):
                resQuad = algo.quadTrap(a,b,p,myf)
            if (choixQuad == "2"):
                resQuad = algo.quadGauss(a,b,p,myf)
            if (choixQuad == "3"):
                resQuad = algo.quadHerm(a,b,p,myf,mydf) 
                
            res[ix,:] = resQuad
            
        res = np.array(res)
        res = res.T
        
        # Affichage de la solution :
        affichage.afficherSol2D(listX,listY,res)
        #affichage.afficherSol3D(listX,listY,res)


    if (choix=="2"):

        # Point (x,y) où on évalue la fonction u
        dx = 0.01
        dy = 0.01
        listX = np.arange(dx,5+dx*0.5,dx)
        listY = np.arange(-2.5,2.5+dy*0.5,dy)
        
        # Frequence ww et attenuation eps
        # Modifier ICI:
        ww = 10.0
        eps = 1.0j
        y1 = 1;
        y2 = -1;
        
        p = 100
        res1 = np.zeros((len(listX),len(listY)),dtype=complex)
        res2 = np.zeros((len(listX),len(listY)),dtype=complex)
        for ix,x in enumerate(listX):
            resy = []
            # Completer ICI :
            myf1 = lambda xi : np.exp(-1.0j*xi*(listY - y1)) * np.exp(1.0j * cmath.sqrt(ww**2 + 1.0j * eps - xi**2) * x)
            mydf1 = lambda xi : ( (-1.0j*listY - (1.0j*xi*x)) / cmath.sqrt(ww**2 + 1.0j*eps - xi**2) ) * myf1(xi)
            
            myf2 = lambda xi : np.exp(-1.0j*xi*(listY - y2)) * np.exp(1.0j * cmath.sqrt(ww**2 + 1.0j * eps - xi**2) * x)
            mydf2 = lambda xi : ( (-1.0j*listY - (1.0j*xi*x)) / cmath.sqrt(ww**2 + 1.0j*eps - xi**2) ) * myf2(xi)

            # Modifier ICI :
            a = -30.0
            b = 30.0
            resQuad1 = 0.0
            resQuad2 = 0.0
            if (choixQuad == "1"):
                resQuad1 = algo.quadTrap(a,b,p,myf1)
                resQuad2 = algo.quadTrap(a,b,p,myf2)
            if (choixQuad == "2"):
                resQuad1 = algo.quadGauss(a,b,p,myf1)
                resQuad2 = algo.quadGauss(a,b,p,myf2)
            if (choixQuad == "3"):
                resQuad1 = algo.quadHerm(a,b,p,myf1,mydf1) 
                resQuad2 = algo.quadHerm(a,b,p,myf2,mydf2) 

            res1[ix,:] = resQuad1
            res2[ix,:] = resQuad2
            
        res1 = np.array(res1)
        res1 = res1.T

        res2 = np.array(res2)
        res2 = res2.T
        
        # Affichage de la solution :
        affichage.afficherSol2D(listX,listY,res1+res2)
        #affichage.afficherSol3D(listX,listY,res)
##----------------------------------    


print("FIN \n")
########################################
