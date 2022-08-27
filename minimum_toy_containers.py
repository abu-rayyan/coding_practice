#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 21:44:42 2022
https://www.hackerrank.com/challenges/priyanka-and-toys/problem
@author: sajid
"""
A=[1, 2, 3, 21, 7, 12, 14, 21]
A.sort()
containers=1
i=0
min_num=A[0]
while i <len(A):    
    if (A[i]-min_num>4):
        containers+=1
        min_num=A[i]

    i+=1
    