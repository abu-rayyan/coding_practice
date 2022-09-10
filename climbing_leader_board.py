#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 17:02:09 2022
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
@author: sajid
"""


my_dict={}
ranked=[100, 100, 50, 40, 40, 20, 10]
ranked=[100, 90, 90, 80, 75, 60]

ranking_set=list(set(ranked))
ranking_set.sort(reverse=True)





    
player=[5, 25, 50, 120]
player=[50, 65, 77, 90, 102]

final_scores=[]

end_counter=len(ranking_set)

for s  in range (0,len(player)):
    print ("===============================")
    print ("score is:", player[s])
    if player[s]==player[s-1]:
        max_value=final_scores[-1]
    if player[s]< ranking_set[-1]:        
        max_value=len(ranking_set)+1
    else:
        for i in range (0, end_counter):
    
            print ("ranking list elemet is:",ranking_set[i])
            if player[s]>= ranking_set[i]:
                print ("matched ranking list elemet is:",ranking_set[i])
                max_value= i+1
                break
        
        print ("max value is;", max_value)        
        
        if max_value<len(ranking_set):
            end_counter=max_value
            print ("end counter is:", end_counter)
    final_scores.append(max_value)
    
            
        

    