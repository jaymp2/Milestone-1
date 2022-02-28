# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 21:16:46 2022

@author: Jack
"""
#p2 + 2pq + q2 = 1
import math
def mendels_law(hom, het, rec):
    
    parents = hom + het + rec
    dom_gen = 2*hom + het
    res_gen = 2 * rec + het
    genes = 2* parents
    possible_off = parents*(parents-1)*4
    paths_off = (hom * ((hom-1) + het+rec) + het*(het-1+hom+rec) + rec * (hom+rec-1+het))*4
    paths_domoff = (4*hom * ((hom-1) + het+rec)+ het*(3*(het-1)+4*hom+2*rec)+ rec * (4*hom+0*(rec-1)+2*het))
    print (paths_domoff)
    print (paths_off) 
    print ( possible_off)
    prob = 100*(paths_domoff/paths_off)
    #possible_off = -1
    #possible_domoff = 4*2*(hom*(hom-1)) + 4*2*(hom*(het)) + 4*2*(hom * rec) + (3)*2*(het*(het-1))+ 2*het*rec*2
    #possible_resoff = (rec *(rec-1)) + (het*(rec-1)/2) + (rec*(het-1)/2) + (1/4)*(het*(het-1))
    #possible_resoff = (math.factorial(rec *(rec)) + .5*math.factorial(het*(rec)) + .25*math.factorial((het*(het))))
    #prob = 1- possible_resoff/(possible_off)
    #print( possible_resoff)
    #print (possible_off)
    #print (possible_domoff)
    #print (res_gen)
    #print (genes)
    #prob = ((res_gen)/(genes)-(res_gen-1)/(genes))
    print (prob)
mendels_law(0,4,0)