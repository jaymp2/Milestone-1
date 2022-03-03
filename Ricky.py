# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:49:51 2022

@author: jaypa
"""
import M1

#rna2codon

table = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'UAU':'Y',
     'UAC':'Y', 'UAA':'Stop', 'UAG':'Stop', 'UGU':'C', 'UGC':'C', 'UGA':'Stop', 'UGG':'W', 'CUU':'L',
     'CUC':'L', 'CUA':'L', 'CUG':'L', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'CAU':'H', 'CAC':'H',
     'CAA':'Q', 'CAG':'Q', 'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AUU':'I', 'AUC':'I', 'AUA':'I',
     'AUG':'M', 'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
     'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R', 'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V', 'GCU':'A',
     'GCC':'A', 'GCA':'A', 'GCG':'A', 'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E', 'GGU':'G', 'GGC':'G',
     'GGA':'G', 'GGG':'G'}
def rna2codon(rna):
    output = ""
    for i in range(0,len(rna)-3,3):
        output += table[rna[i:i+3]]
    return output
string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

print(rna2codon(string))

#source_rna

def source_rna(protein):
    count=0   
    for key in table.keys():
        if table[key] in protein:
            count+=1
        elif table[key]=='*':
            count+=len(protein)

    return count%1000000

print(source_rna("MA"))

#reverse_compliment

def reverse_complement(dna):
    dna = dna[::-1]
    ans = ""
    for ch in dna:
        if ch == "A":
            ans += "T"
        elif ch == "C":
            ans += "G"
        elif ch == "T":
            ans += "A"
        elif ch == "G":
            ans += "C"

    return ans
