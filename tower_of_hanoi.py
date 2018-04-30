# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 18:19:15 2018

@author: Administrator

"""

class Tower:
    """Course-Week2:Simple Programs-4.Functions-Video:TowersofHanoi-method1
        
    """

    def __init__(self):
        self.counter = 0
        
    def hanoi(self, n, a, c, b):
        if n == 1: 
            self.counter += 1
            print('count ' + str(self.counter) + ', move from {0}->{1}'.format(a, b))
            
        else:
            self.hanoi(n-1, a, b, c)
            self.hanoi(1, a, c, b)
            self.hanoi(n-1, b, c, a)    
   
tower = Tower()
tower.hanoi(4,"a", "c", "b")


    
def Towers(n,fr,to ,spare):
    """Course-Week2:Simple Programs-4.Functions-Video:TowersofHanoi-method2
        
    """

    if n==1:
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr) 

def printMove(fr,to):
    global count 
    count+=1
    print('count '+str(count)+", move from "+ str(fr)+" to "+str(to))

count = 0 
Towers(4,'a','b','c')

