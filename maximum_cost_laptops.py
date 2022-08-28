#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 23:25:31 2022

@author: sajid
"""
# cost=[0,3,2,3,4]
cost=[3, 2, 0, 2, 4, 0, 1, 4]
# labels=["legal", "legal", "illegal", "legal", "legal"]
labels=['legal', 'illegal', 'legal', 'legal', 'illegal', 'legal', 'legal', 'legal']
# dailyCount=1
dailyCount=4
print ("cost is:", cost)
print ("labels are:", labels)
print ("daily count is:", dailyCount)
i=0
j=i
cost_list=[]
while i<len(cost):
    i=j
    d_cost=0
    l_count=0
    print ("count list is:", cost_list)
    while j<len(cost):
        d_cost=d_cost+cost[j]
        print ("cost is:", d_cost)
        if labels[j]=="legal":
            l_count=l_count+1
            if l_count>=dailyCount:
                cost_list.append(d_cost)
                print ("cost list is:", cost_list)
                j=j+1
                i=j
                break
        else:
            j=j+1
            i=j
max_cost=max(cost_list)