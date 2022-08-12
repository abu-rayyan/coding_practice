#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:58:10 2022

# Complete the makeAnagram function below.
cde
abc
def makeAnagram(a, b):
"""
a="fcrxzwscanmligyxyvym"
b="jxwtrhvujlmrpdoqbisbwhmgpmeoke"

a_set=set(a)
b_set=set(b)
a_len=len(a_set)
b_len=len(b_set)


if a_len<b_len:
    small_str=a
    large_str=b
else:
    small_str=b
    large_str=a       


large_dict={}
for c in large_str:
    large_dict[c]=large_dict.setdefault(c, 0)+1
count=0    
for key in large_dict.copy():
    if key not in small_str:
        count=count+large_dict[key]
        if key in large_dict:
            del large_dict[key]
        
small_dict={}
for c in small_str:
    small_dict[c]=small_dict.setdefault(c, 0)+1           

 
for key, value in small_dict.items():
    diff=0    
    if key not in large_dict:
        count=count+small_dict[key]
    elif value!= large_dict[key]:
        diff=abs(value-large_dict[key])
    count=count+diff
    
    







