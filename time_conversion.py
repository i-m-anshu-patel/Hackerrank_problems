# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:40:30 2021

@author: HP
"""


c = [4,4,1,3]

print(c.count(max(c)))


a= '01:05:45PM'

    
def timeConversion(s):
    if s[-2]=="A":
        x = s.split(':')
        if x[0]=='12':
            x[0]='00'
        if len(x[0])==1:
            x[0]='0'+x[0]
        x[-1]=x[-1][0:-2]
        return ':'.join(x)
    else:
        y = s[0:-2]
        x = s.split(':')
        if x[0]!='12':
            x[0]=str((int(x[0])+12)%24) 
        if len(x[0])==1:
            x[0]='0'+x[0]
        x[-1]=x[-1][0:-2]
        return ':'.join(x)
    
print(timeConversion(a))
print(timeConversion('06:40:03AM'))
print(timeConversion('12:45:54PM'))
print(timeConversion('12:40:22AM'))
