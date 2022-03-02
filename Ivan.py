dna="GATGGAACTTGACTACGTAAATT"
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
