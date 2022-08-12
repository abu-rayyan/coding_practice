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

count=0  
for element in large_str:
    if element not  in small_str:
        large_str =large_str.replace(element,"", 1)
        print ("large str is:", large_str)
        count=count+1

large_dict={}
for c in large_str:
    large_dict[c]=large_dict.setdefault(c, 0)+1


small_dict={}
for c in small_str:
    small_dict[c]=small_dict.setdefault(c, 0)+1
    
    
for element in small_str:
    if element not in large_str:
        small_dict.pop(element, None)
        count=count+1

for key, value in large_dict.items():
    diff=0
    
    print ("===================================")
    print ("key is:", key)
    print ("value is:", value)
    if value!= small_dict[key]:
        diff=abs(value-small_dict[key])
    count=count+diff

        
        



