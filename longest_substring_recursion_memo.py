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

def lcs_memo( i=0, j=0):
    key=(i, j)
    if key in memo:
        return memo[key]
    if i==len(s1) or j==len(s2):
        memo[key]=0
    elif s1[i]==s2[j]:
        memo[key]= 1 + lcs_memo( i+1, j+1)
    else:
        option_1=lcs_memo(i+1, j)        
        option_2=lcs_memo( i, j+1)
        memo[key]= max(option_1, option_2)
    
    return memo[key]
m=lcs_memo(i=0, j=0)