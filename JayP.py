# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:49:51 2022

@author: jaypa
"""
#define the function
def s(dna):
    
    #make the initial dictionary to store the count
    count = {'A':0,'C':0,'G':0,'T':0}
    
    #goes through the string "dna" and for each letter, runs the "for" loop
    for nucleotide in dna:
        #when the letter is found to be "A", the count in the dictionary goes up by 1 for "A"
        if nucleotide == 'A':
            count['A'] += 1
    
        #when the letter is found to be "C", the count in the dictionary goes up by 1 for "C"
        if nucleotide == 'C':
            count['C'] += 1
            
        #when the letter is found to be "G", the count in the dictionary goes up by 1 for "G"
        if nucleotide == 'G':
            count['G'] += 1
            
        #when the letter is found to be "T", the count in the dictionary goes up by 1 for "T"
        if nucleotide == 'T':
            count['T'] += 1
            
    return count 


def locate_substring(dna_snippet, dna):
    if dna_snippet in dna:
        
    