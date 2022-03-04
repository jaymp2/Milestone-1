dna = "GATGGAACTTGACTACGTAAATT"
def dna2rna(dna):
    rna = ''
    for symbol in dna:
        if symbol == 'A':
            rna = rna + 'A'
        elif symbol == 'C':
            rna += 'C'
        elif symbol == 'G':
            rna += 'G'
        elif symbol == 'T':
            rna += 'U'
    return rna
print(dna2rna(dna))

def count_dom_phenotype(genotype):
    a = int(genotype[0])
    b = int(genotype[1])
    c = int(genotype[2])
    d = int(genotype[3])
    e = int(genotype[4])
    f = int(genotype[5])
    if genotype[0] >= 1:
        genotype[0] = 1
    else:
        genotype[0]=0
    if genotype[1] >= 1:
        genotype[1] = 1
    else:
        genotype[1]=0
    if genotype[2] >= 1:
        genotype[2] = 1
    else:
        genotype[2]=0
    if genotype[3] >= 1:
        genotype[3] = 1
    else:
        genotype[3]=0
    if genotype[4] >= 1:
        genotype[4] = 1
    else:
        genotype[4]=0
    if genotype[5] >= 1:
        genotype[5] = 1
    else:
        genotype[5]=0
        genotype = [a,b,c,d,e,f]
    return (((2 * a) + (2 * b) + (2 * c) + ((3/2) * d)+ e + (0 * f)))

def gc_content(dna_list):
    gc_letters = 'GC'
    i=0
    gc_content_list = []
    while i in range(len(dna_list)):
        gc_count=0
        dna = dna_list[i]
        for letters in dna:
            if letters in gc_letters:
                gc_count = gc_count + 1
        gc_count = (gc_count/len(dna))*100
        gc_content_list.append(gc_count)
        i = i + 1
    highest_gc = max(gc_content_list)
    max_index = gc_content_list.index(highest_gc)
    return max_index, highest_gc

#rna2codon

table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',

        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',

        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',

        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }
def rna2codon(rna):
    def triplet2codon(triplet):
        allowed_codons = set('AGCU')
        return table.get(triplet.upper(), 'Invalid')
    amino = ''
    for i in range (0, int(len(rna)/3)):
        x = triplet2codon(rna[3*i:3*i+3])
        if x == '*':
            return amino
        else:
            amino += x
    return amino

string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

print(rna2codon(string))



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
