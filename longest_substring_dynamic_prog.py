#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 13:09:39 2022

@author: sajid
"""

s1="analogy"
s2="alchemy"


s1="absent"
s2="best"


s1="serendipitous"
s2="precipitation"

memo={}

def lcs_dp( i=0, j=0):
    n1, n2= len(s1), len(s2)
    table =[[0 for x in range (n2+1)] for x in range (n1+1)]
    for i in range (n1):
        for j in range (n2):
            if s1[i]==s2[j]:
                table[i+1][j+1]=1+ table[i][j]
            else:
                table[i+1][j+1]=max(table[i][j+1], table [i+1][j])
    return table[-1][-1]              

m=lcs_dp(i=0, j=0)