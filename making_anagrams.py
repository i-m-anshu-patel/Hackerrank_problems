# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:39:19 2021

@author: HP
"""
'''

Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams.
 Any characters can be deleted from either of the strings.

Example


Delete  from  and  from  so that the remaining strings are  and  which are anagrams. This takes  character deletions.

Function Description

Complete the makeAnagram function in the editor below.

makeAnagram has the following parameter(s):

string a: a string
string b: another string
Returns

int: the minimum total characters that must be deleted
Input Format

The first line contains a single string, .
The second line contains a single string, .

Constraints

The strings  and  consist of lowercase English alphabetic letters, ascii[a-z].
Sample Input:
cde
abc
Sample Output:
4
Explanation
Delete the following characters from the strings make them anagrams:
Remove d and e from cde to get c.
Remove a and b from abc to get c.
It takes 4 deletions to make both strings anagrams.
'''

def makeAnagram(a, b):
    if len(a)>len(b):       
        large = sorted(a)
        small = sorted(b)
    else:
        large = sorted(b)
        small = sorted(a)
    res=[]                      
    for i in range(len(large)):
        if large[i] in small:
            small.remove(large[i])
            res.append(large[i])
    return ((len(large)-len(res))+len(small))       

            
    
print(makeAnagram('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'))
print(makeAnagram('showman', 'woman'))

# a = [1,2,3]
# b=[3]
# for i in a:
#     if i in b:
#         print("ooo yesah")