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

a=1
b=0
c=0
d=1
e=0
f=1
couple = [a,b,c,d,e,f]
def count_dom_phenotype(couple):
    return (((2 * a) + (2 * b) + (2 * c) + ((3/2) * d)+ e + (0 * f)))
def genotype():   
    a = int(couple[0])
    b = int(couple[1])
    c = int(couple[2])
    d = int(couple[3])
    e = int(couple[4])
    f = int(couple[5])
print(count_dom_phenotype(couple))



