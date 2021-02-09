# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:38:06 2021

@author: HP
"""


a = 'SHINCHAN'
b= 'NOHARAAA'
# def commonChild(s1, s2):
#     unique_s1= set(s1)
#     unique_s2= set(s2)
#     common = []
#     for i in unique_s1:
#         if i in unique_s2:
#             common.append(i)
#     sum_of_all=0
#     for i in common:
#         sum_of_all+=min(s1.count(i), s2.count(i))
#     return sum_of_all


# Dynamic Programming implementation of LCS problem 

def LCS(s1, s2):
    n, m = len(s1), len(s2)
    lcs = [[0] * (m + 1) for _ in xrange(n + 1)]

    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

    return lcs[n - 1][m - 1]


if __name__ == '__main__':
    a = raw_input()
    b = raw_input()

    print LCS(a, b)



# Driver program to test the above function 
# X = "AGGTAB"
# Y = "GXTXAYB"
# print("Length of LCS is ", lcs(X, Y)) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 


# def commonChild(s1, s2):
#     lst=[]
#     for i in s1:
#         if i in s2:
#             lst.append(s2.index(i))
#     print(lst)
#     mylst= [lst[0]]
#     for i in lst[1:]:
#         if i not in mylst:
#             if i<mylst[-1]:
#                 mylst=[i]
#             else:
#                 mylst.append(i)
#     return len(mylst)

# # A Naive recursive Python implementation of LCS problem 

# def lcs(X, Y, m, n): 

# 	if m == 0 or n == 0: 
# 	return 0; 
# 	elif X[m-1] == Y[n-1]: 
# 	return 1 + lcs(X, Y, m-1, n-1); 
# 	else: 
# 	return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 


# # Driver program to test the above function 
# X = "AGGTAB"
# Y = "GXTXAYB"
# print ("Length of LCS is ", lcs(X, Y, len(X), len(Y))) 

    

print(commonChild(a,b))
print(commonChild('HARRY', 'SALLY'))
print(commonChild('OUDFRMYMAW', 'AWHYFCCMQX'))
print(commonChild('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS', 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'))

