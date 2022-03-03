dna = "TACGATCGATCGTCTTCAG"
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



