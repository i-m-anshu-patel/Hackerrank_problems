# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:45:27 2021

@author: HP
"""




def cuboid(x,y,z,n):
    return [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c !=n]

print(cuboid(1,1,1,2))
print(cuboid(2,2,2,2))
print(cuboid(1,1,2,3))
print(cuboid(4,5,6,-10))
print(cuboid(5,5,5,8))
print(cuboid(3,6,5,14))
