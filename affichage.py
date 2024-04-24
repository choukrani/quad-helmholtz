#!/usr/bin/python3
#-*- coding: utf-8 -*-

#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
import numpy as np

import data
    

##----------------------------------   
def afficherQuad(a,b,p,f,choixQuad):
    h = (b-a)/p
    xx = np.arange(a,b,max(h*0.01,1e-3))
    yy = f(xx)
    
    plt.plot(xx,yy, '-',color='#2ca02c',linewidth=2.0)        
    
    x = a
    while(x < b-1e-8):
        # if(choixQuad =="-1"):
#             plt.plot([x,x+h],[f(x+0.5*h),f(x+0.5*h)],'--',color='#1f77b4',linewidth=2.0)
#             plt.plot([x,x],[0.0,f(x+0.5*h)],'k--',linewidth=1.0)
#             plt.plot([x+0.5*h],[f(x+0.5*h)],'x',color='#ff7f0e')
#         if(choixQuad =="0"):
#             plt.plot([x,x+h],[f(x),f(x)],'--',color='#1f77b4',linewidth=2.0)
#             plt.plot([x,x],[0.0,f(x)],'k--',linewidth=1.0)
#             plt.plot([x],[f(x)],'x',color='#ff7f0e')
        if(choixQuad =="1"):
            plt.plot([x,x+h],[f(x),f(x+h)],'--',color='#1f77b4',linewidth=2.0)
            plt.plot([x,x],[0.0,f(x)],'k--',linewidth=1.0)
            plt.plot([x],[f(x)],'x',color='#ff7f0e')
        if(choixQuad == "2"):
            xh = np.arange(x,x+h+h*0.01,h*0.1)
            x1 = x+h*(1.0-1.0/np.sqrt(3.0))*0.5
            x2 = x+h*(1.0+1.0/np.sqrt(3.0))*0.5
            yh = f(x1) * (xh-x2) / (x1-x2)
            yh += f(x2) * (xh-x1)/ (x2-x1)
            
            plt.plot(xh,yh,'--',color='#1f77b4',linewidth=2.0)
            plt.plot([x,x],[0.0,f(x)],'k--',linewidth=1.0)
            plt.plot([x1,x2],[f(x1),f(x2)],'x',color='#ff7f0e')
        if(choixQuad == "3"):
            xh = np.arange(x,x+h+h*0.01,h*0.1)
            x1 = x+h*0.5
            yh = f(x1) + 0*xh
            x0 = x
            x2 = x+h
            df0 = data.df(x0)
            df2 = data.df(x2)
            
            aa = 0.5*(df0 + df2)
            bb = 0.5*(df2 - df0)/h
            yh += (xh - x1)*aa + ((xh-x1)**2)*bb
            plt.plot(xh,yh,'--',color='#1f77b4',linewidth=2.0)
            plt.plot([x,x],[0.0,f(x)],'k--',linewidth=1.0)
            plt.plot([x1],[f(x1)],'x',color='#ff7f0e')
            
        x = x+h
    plt.plot([b,b],[0.0,f(b)],'k--',linewidth=1.0)
    if(choixQuad == "1" or choixQuad == "2"):
        plt.plot([b],[f(b)],'x',color='#ff7f0e')    
    plt.legend(["f","Interp"])
    
    
    
    axes = plt.gca()
    axes.set_xlim(a-0.1,b+0.1)
    axes.set_ylim(min(min(yy),0.0)-0.1,max(max(yy),0.0)+0.1)
    # turn off the right spine/ticks
    axes.spines['right'].set_color('none')
    axes.yaxis.tick_left()

    # set the y-spine
    axes.spines['bottom'].set_position('zero')

    # turn off the top spine/ticks
    axes.spines['top'].set_color('none')
    axes.xaxis.tick_bottom()
    
    
    
    plt.show()
    
##----------------------------------   

##----------------------------------   
def afficherConv(list_x,list_y):
    for j,absic in enumerate(list_x):
        plt.plot(absic,list_y[j], 'x-',linewidth=4.0)
    
    plt.legend(["log10(err) vs log10(p)"])
    plt.show()    
##----------------------------------   

##----------------------------------
#  Affichage 1D :        
def afficher1Dbis(list_x,list_y):
    #plt.hold('on')
    
    plt.plot(list_x[0],list_y[0], 'b-',linewidth=2.0)
    plt.plot(list_x[1],list_y[1], 'r-',linewidth=2.0)
    plt.plot(list_x[2],list_y[2], 'bx',linewidth=4.0)
    plt.plot(list_x[3],list_y[3], 'rx',linewidth=4.0)
    
    plt.legend(["interp Xt","interp Yt","XX","YY"])
    plt.show()
    #plt.hold('off')
##----------------------------------    
    
    
    
    
##----------------------------------  
#  Affichage 2D :      
def afficherSol2D(ptX,ptY,Val):
    
    ptX, ptY = np.meshgrid(ptX, ptY)
    
    plt.pcolor(ptX,ptY,np.real(Val),cmap=cm.jet)
    plt.axis('equal')
    plt.colorbar()
    plt.show()


def afficherSol3D(ptX,ptY,Val):
    
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    
    ptX, ptY = np.meshgrid(ptX, ptY)
    # Affichage surface MNT :
    surf = ax.plot_surface(ptX, ptY, np.real(Val), cmap=cm.jet, linewidth=0, antialiased=False, shade=False)#

    plt.show()
##----------------------------------    
##----------------------------------    

