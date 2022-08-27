#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 16:14:08 2022

@author: sajid
"""

def rev_str(s):
    x = list(filter(str.isalpha, s[::-1]))
    for i,s_ in enumerate(s):
        if not s_.isalpha():
            x.insert(i, s_)
    return ''.join(x)

st = 'b3ghcd hg#tyj%h'
output = ' '.join(rev_str(s) for s in st.split())



