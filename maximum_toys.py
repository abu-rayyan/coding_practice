#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 13:47:31 2022
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.

Note Each toy can be purchased only once.

Example

The budget is units of currency. He can buy items that cost for , or for units. The maximum is

items.

Function Description

Complete the function maximumToys in the editor below.

maximumToys has the following parameter(s):

    int prices[n]: the toy prices
    int k: Mark's budget

Returns

    int: the maximum number of toys

Input Format

The first line contains two integers,
and , the number of priced toys and the amount Mark has to spend.
The next line contains space-separated integers

Constraints




A toy can't be bought multiple times.

Sample Input

7 50
1 12 5 111 200 1000 10

Sample Output

4

Explanation

He can buy only 4
toys at most. These toys have the following prices: 1, 12, 5, 10
@author: sajid
"""
prices=[1 ,12 ,5 ,111, 200 ,1000 ,10]
prices=[1, 12, 5 ,111 ,200 ,1000, 10]
k=50
# prices=[1 12 5 111 200 1000 10]
prices=[x for x in prices if x<=k]
prices.sort()
my_sum=0
count=0
for i in range (len(prices)):
    my_sum=prices[i]+my_sum
    if my_sum>=k:
        break
    else:
        count=count+1

