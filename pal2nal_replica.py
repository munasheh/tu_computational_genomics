
##pal2nal
##write a python script that replicates pal2nal

##import modules
from Bio import SeqIO
import textwrap
import itertools


print('This is a python script that replicates pal2nal')

print('pal2nal is a program that converts a protein alignment and the corresponding nucleotide sequences into a codon alignment')
print('This program only works with files in fasta format. Please do not use any non-fasta files')
##upload the protein sequence alignment and the nucleotide sequences
print('Protein Alignment file must be in fasta format.')
#pa = ('protein.fasta')
pa =  input('Please enter the name of the protein alignment file here: ')
print('File of nucleotide sequences must correspond exactly to amino acid sequences in Protein Alignment file!')
print('Nucleotide file must be DNA or use Thymine instead of Uracil for mRNA')
print('Output will use T only')
print('This program may not work on files with dashes')

#nuca = 'nucapractice.fasta'
nuca = input('Please enter the name of the nucleotide file. ')

#nucleotide_seq = open(nuca,'r')
#open dictionary for nucleotide files 
nucleotide_dict = {}
nucleotide_list = []
for nucrecord in SeqIO.parse(nuca,'fasta'):
    nucsequence = nucrecord.seq
    # nucleotide_dict[nucrecord.id] = str(nucsequence.strip())
    # print(textwrap.wrap("123456789", 2))
    nucseqlist = textwrap.wrap(str(nucsequence.strip()), 3)
    # nucseqlist = list(str(nucsequence.strip()))
    nucleotide_list.append([nucrecord.id] + nucseqlist)

# print(nucleotide_list) #works

##open dictionary for AA file
protein_dict = {} 
##read in the file so that the program can get to the data/ use readlines for this
for record in SeqIO.parse(pa,'fasta'):
    sequence = record.seq
    protein_dict[record.id] = str(sequence.strip())

def write_output(nucleotide, possible_codon):
    output2 = nucleotide[0] +'\t'+ ''.join(nucleotide[1:]) + '\n'
    print(output2)
    with open ('outputfile2.txt', 'a') as out2:
        out2.write(output2)

##stop codons are not included in this table
dnatable = {
    'F':['TTT','TTC'],
    'L':['TTA','TTG'],
    'S':['TCT','TCC','TCA','TCG','AGT','AGC'],
    'Y':['TAT','TAC'],
    'C':['TGT','TGC'],
    'W':['TGG'],
    'L':['CTT','CTC','CTA','CTG'],
    'P':['CCA','CCC','CCA','CCG'],
    'H':['CAT','CAC'],
    'Q':['CAA','CAG'],
    'R':['CGT''CGC','CGA','CGG',],
    'I':['ATT','ATC','ATA'],
    'M':['ATG'],
    'T':['ACT','ACC','ACA','ACG'],
    'N':['AAT','AAC'],
    'K':['AAA','AAG'],
    'R':['AGA','AGG'],
    'V':['GTT','GTC','GTA','GTG'],
    'A':['GCT','GCC','GCA','GCG'],
    'D':['GAT','GAC'],
    'E':['GAA','GAG'],
    'G':['GGU','GGC','GGA','GGG'],
    'X':['XXX']}

for key, protein in protein_dict.items():
    possible_codon = []
    possible_codon_with_dash = []
    for aa in protein:
        if aa in dnatable:
            possible_codon.append(dnatable[aa])
            possible_codon_with_dash.append(dnatable[aa])
        else:
            possible_codon_with_dash.append('---')
        #print(possible_codon_with_dash) works

    break_out_flag = False
    #print(len(possible_codon)) counts the number of nucs in aa
    for nucleotide in nucleotide_list:
        #print(len(nucleotide)) works
        #print(nucleotide) works
        for i in range(0, len(nucleotide)-1):
            #print(i)
            #print('codons: '+ str(possible_codon[1]))
            n = str(nucleotide[i+1])
            #print(n)
            if 'XXX' in possible_codon[i]: continue
            # if i+1 == len(nucleotide)-1:
            #     print(nucleotide)
            if (n not in possible_codon[i]):
                #print('breaking')
                break
            if i+1 == len(nucleotide)-1:
                print(nucleotide)
                write_output(nucleotide,possible_codon)
                break_out_flag = True   
        if break_out_flag:
            break

print('Finished! See outputfile2.txt for result')