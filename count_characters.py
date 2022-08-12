#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:58:10 2022

@author: sajid
"""

"""count a's in infinitely repeating string
def repeatedString(s, n):
    print ("string is:", s)
    print("n is :", n)
    
Debug output

    string is: aba

    n is : 10

"""
n=1000000000000
s="a"
a_count=s[:n%len(s)].count('a')+(s.count('a')*(n//len(s)))



    