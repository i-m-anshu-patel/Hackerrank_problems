# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:13:45 2021

@author: HP
"""
'''
fast solution

from collections import Counter

def isValid(s):
    c = Counter(Counter(s).values())
    if len(c)==1:
        return "YES"
    if len(c)>2:
        return "NO"
    if 1 in c.values() and (c[min(c.keys())]==1 or (max(c.keys()) - min(c.keys())==1)):
        return "YES"
    else:
        return "NO"

'''

def isValid(s):
    b = set(s)
    lst=[]
    if len(b)==len(s):
        return "YES"
    for i in b:
        lst.append(s.count(i))
    myset= set(lst)
    mylst=[i for i in myset]
    if len(mylst)>2:
        return "NO"
    else:
        x = mylst[0]
        y = mylst[1]
        if x+1==y:
            if (lst.count(x)==1 or lst.count(y)==1):
                return "YES"
            else:
                return "NO"
        else:
            if x==1 and lst.count(x)==1:
                return "YES"
            else:
                return "NO"
            
print(isValid('aabbccddeefghi'))
print(isValid('aaaaabc'))
print(isValid("a"))