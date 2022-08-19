#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 14:24:33 2022

@author: sajid
You are given two strings str1 and str2. You have to check if the two strings
share a common substring.
Input : str1 = "HELLO"
        str2 = "WORLD"
Output : YES
Explanation :  The substrings "O" and
"L" are common to both str1 and str2

Input : str1 = "HI"
        str2 = "ALL"
Output : NO
Explanation : Because str1 and str2 
have no common substrings
"""

s1="hello"
s2="world"

for ch in s1:
    if ch in s2:
        print("got a common sub str as:", ch)
        break
    
        