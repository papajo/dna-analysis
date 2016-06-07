'''read a DNA sample from a suspect, compare it to a DNA sample from the crime
scene, and let the user know whether the suspect is a criminal.'''
sample = ['GTA','GGG','CAC']
def read_dna(dna_file):
    dna_data = ""
    with open (dna_file, "r") as f:
       for line in f:
           dna_data += line
       return dna_data
'''a method that will iterate through a string, slice it into smaller strings
that are 3 letters long, and add them to a list. This functionality will help us
match the sample to a suspect's DNA later.'''
def dna_codons(dna):
    codons = []
    for i in range(0, len(dna), 3):
        if (i+3) < len(dna):
            codons.append(dna[i:i+3])

    return codons

'''a method that will iterate through both the sample and a suspect's DNA.
  The method should count the number of times a codon in the sample matches a
  codon in the suspect's DNA.'''
def match_dna(dna):
    matches = 0
    for codon in dna:
        if codon in sample:
           matches += 1
           
    return matches

def is_criminal(dna_sample):
    dna_data = read_dna(dna_sample)
    codons = dna_codons(dna_data)
    num_matches = match_dna(codons)
    if num_matches >= 3:
       print "Number of matches %s suspect could be a criminal" %(num_matches)
    else:
       print "Number of matches %s suspect can be freed" %(num_matches)

#is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
#is_criminal("suspect3.txt")
