# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 22:00:24 2021

@author: HP
"""

def palin(x):
    if x==x[::-1]:
        if len(set(x))==1 or len(set(x))==2:
            return True
        else:
            return False
    else:
        return False
    
def special_string(string):
    result=[]
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            r= string[i:j]
            if palin(r):
                result.append(r)
    return len(result)

#Faster Alternative
'''
1. Build a list of tuples such that the string "aaabbc" can be
 squashed down to [("a", 3), ("b", 2), ("c", 1)]. 
 2. add to answer all combinations of substrings from these tuples 
 which would represent palindromes which have all same letters. 
 3. traverse this list to specifically find the second case mentioned in probelm

def substrCount(n, s):
    l = []
    count = 0
    cur = None

# 1st pass
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    ans = 0
		
# 2nd pass
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

# 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans
'''


print(special_string('mnonopoo'))
print(special_string('asasd'))
print(special_string('abcbaba'))
print(special_string('aaaa'))