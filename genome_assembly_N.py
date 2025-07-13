##write a python program that calculates N? for a genome assembly
##command line terms: fasta file of assembled contigs, the N value, actual size of the genome
## Turn in: Python Script, Text file with the results

##import modules
from Bio import SeqIO
import sys
import numpy
import os

#commandline argument 
#argv[1] = fasta file
#argv[2] = ? part of N number
#argv[3] = actual size of genome

# print('Please enter the name of your fasta file: ')
# if "." not in sys.argv[1] :
#     print(sys.argv[1] + " is not a file")
#     exit()
# if 
input = open(sys.argv[1]) ##this wil be the name of the fasta file
#input = open('contigs.fa')

seqlength = []

for record in SeqIO.parse (input, 'fasta'): 
    bp = len(record.seq)
    seqlength.append(bp)

##get the other command line arguments?

N = int(sys.argv[2]) # this is the ? part of the N? number. probs should put a statment here saying that it needs to be between 10 and 90
# N = int(N)
gl = sys.argv[3] #this is the actual size of the genome

seqlength = sorted(seqlength)

unique = []


for entry in seqlength:
    if not entry in unique:
        unique.append(entry)

N_value = []

for entry in unique:
    multiplier = seqlength.count(entry) * entry
    for i in range(multiplier):
        N_value.append(entry)
    
index = len(N_value)*(N/100) # change 0.5 to the N PERCENTAGE
avg = []


if index % 2 == 0 :
    first = N_value[index-1]
    second = N_value[index]
    avg.append(first)
    avg.append(second)
    N_value = numpy.mean(avg)
    print (' the N_value is : %d'%N_value)
else: 
    print('Done')
    print(N_value[int(index-1)+1])
    # print('the N_value is: %d' %N_value[index -1])
input.close()



# python /week4_part2.py contigs.fa 50 500000
# 7789 or 1115