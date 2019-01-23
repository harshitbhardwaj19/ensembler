# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from collections import Counter
data=pd.read_csv('ensemble.csv')

X=data.iloc[:,1:16].values
X

import random
z=[]
max_acc=0
bestcombi=[]
actual=data.iloc[:,0].values
for i in range (1,110):
    x=random.randrange(1,15,2)
    for j in range(1,x+1):
        while True:
            y=random.randrange(1,15)
            if y not in z:
                z.append(y)
                break
                
    #print(z)
    #print()
          
    
    test=data.iloc[:,z].values
    
    pred=[]
    corr=0
    
    for j in range(0,len(test)):
       a=Counter(test[j])
       #if test[j].Counter(1)>test[j].count(0):
       if a[1]>a[0]:
           pred.append(1)
       else:
           pred.append(0)    
        
       if pred[j]==actual[j]:
           corr=corr+1
    #print(corr)
    acc=corr*100/len(test)
    #print(acc)
    if(max_acc<acc):
        max_acc=acc
        bestcombi.clear()
        bestcombi.extend(z)           
    z.clear()
    
print(max_acc)
print(bestcombi)    
    
    
#z=[1,2,3,4,5]
#if 6 in z:
#    print("hello") 
    