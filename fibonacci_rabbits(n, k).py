# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 23:04:59 2022

@author: Jack
"""

def fibonacci_rabbits(n, k):
    months = n
    bre_pairs = 1
    bab_pairs = 0
    while months > 1:
        months = months - 1
        new_bab_pairs = bre_pairs*k
        bre_pairs = bre_pairs + bab_pairs
        bab_pairs = new_bab_pairs
        #print (bab_pairs)
        print (bre_pairs)
    return bre_pairs
print(fibonacci_rabbits(5, 3))