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


def hamming_dist(dna1,dna2):
    value = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            value += 1
    return value 


def locate_substring(dna_substring, dna):
    result = -1
    first_loop = True
    locations = []
    while (result != -1 or first_loop):
        first_loop = False
        result = dna.find(dna_substring, result + 1)
        if(result != -1):
            locations.append(result)
    return locations
   

table = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'UAU':'Y',
     'UAC':'Y', 'UAA':'Stop', 'UAG':'Stop', 'UGU':'C', 'UGC':'C', 'UGA':'Stop', 'UGG':'W', 'CUU':'L',
     'CUC':'L', 'CUA':'L', 'CUG':'L', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'CAU':'H', 'CAC':'H',
     'CAA':'Q', 'CAG':'Q', 'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AUU':'I', 'AUC':'I', 'AUA':'I',
     'AUG':'M', 'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
     'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R', 'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V', 'GCU':'A',
     'GCC':'A', 'GCA':'A', 'GCG':'A', 'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E', 'GGU':'G', 'GGC':'G',
     'GGA':'G', 'GGG':'G'}
table_values = list(table.values())
def source_rna(protein):
    count = 1
    for i in protein:
        count *= table_values.count(i)
    count *= table_values.count('Stop')
    return count


        

        

        
        
        
