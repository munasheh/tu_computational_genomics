import Bio
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio import Entrez
import sys
from Bio.Blast import NCBIWWW
import random

#get the fasta file
fasta = 'TP53_aa.fasta'
target = int(input('enter the index you are trying to find: '))
#parse the fasta file
for record in SeqIO.parse(fasta, 'fasta'):
    sequence = record.seq
    list(sequence)
    print('target -1: ', sequence[target-1])
    print('target', sequence[target])
    print('target + 1', sequence[target+1])
#do the same for the changed file
fasta2 = str(input('enter the name of the file that you are trying to compare to the original: '))
for record in SeqIO.parse(fasta2, 'fasta'):
    sequence = record.seq
    list(sequence)
    print('target -1: ', sequence[target-1])
    print('target', sequence[target])
    print('target + 1', sequence[target+1])
