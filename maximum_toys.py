#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 13:47:31 2022

@author: sajid
"""
prices=[1 ,12 ,5 ,111, 200 ,1000 ,10]
prices=[1, 12, 5 ,111 ,200 ,1000, 10]
k=50
# prices=[1 12 5 111 200 1000 10]
prices=list(set([x for x in prices if x<=k]))
prices.sort()
my_sum=0
count=0
for i in range (len(prices)):
    my_sum=prices[i]+my_sum
    if my_sum>=k:
        break
    else:
        count=count+1

