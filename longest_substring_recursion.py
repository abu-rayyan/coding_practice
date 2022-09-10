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


def lcs_recursive(s1, s2, i=0, j=0):
    if i==len(s1) or j==len(s2):
        return 0
    elif s1[i]==s2[j]:
        return 1 + lcs_recursive(s1, s2, i+1, j+1)
    else:
        option_1=lcs_recursive(s1, s2, i+1, j)        
        option_2=lcs_recursive(s1, s2, i, j+1)
        return max(option_1, option_2)
    

m=lcs_recursive(s1, s2, i=0, j=0)