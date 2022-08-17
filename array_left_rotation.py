#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:35:44 2022

@author: sajid
"""
def rotate_array(A):


    temp=A[len(A)-1]
    
    for i in range (len(A)):
        print ("===============")
        print ("array before operation is:", A)
        A[i-1]=A[i]
        print ("array after operation is:", A)
    
    A[len(A)-2]=temp
    return A

A=[1, 2, 3, 4, 5]
d=2
for i in range(d):
    A=rotate_array(A)
    