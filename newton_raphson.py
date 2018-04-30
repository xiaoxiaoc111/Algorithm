# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:15:02 2018

@author: Administrator
Newton-Raphson ：
epsilon 代表精度
x,y 代表二元多次方程式

example:  y=5*(x**4)+3*(x**3)+2*(x**2)+6*x+10
          y'=20*(x**3)+9*(x**2)+3*x+6


"""

epsilon=0.01
y=20.0
x=y/2.0
times=0
# equation y=x**2  y'=2x  
# newton-raphson  

while abs(x*x-y)>=epsilon:
    times+=1
    x=x-((x**2)-y)/(2*x)

    
print ("Number_guess_times="+str(times))
print ("Square root of "+ str(y)+"is about"+str(x))

