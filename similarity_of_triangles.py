# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:59:29 2021

@author: HP
"""


side = [[4, 8],[15, 30],[25, 50]]
s= [[2, 1],[10, 7],[9, 6],[6, 9],[7, 3]]
                


def nearlySimilarRectangles(sides):
    count=0
    for i in sides:
        for j in sides:
            if i!=j and i[0]/j[0]==i[1]/j[1]:
                count+=1
    return count//2

print(nearlySimilarRectangles(s))
print(nearlySimilarRectangles(side))