'write a python program to simulate fastq file short-read data'
'program should sample evenly from all portions of the file'
'output file will be in fastq format with each read appearing as one sequence'
'quality line will be generated using a random number generator'
'take 4 command line arguments: input file, output file, length of reads, depth of coverage'

#import modules
from Bio import SeqIO
from Bio.Seq import Seq
import sys
import numpy
import os
import random

#list of commandline arguments:
##sys.argv[1] = input file
##sys.argv[2] = output file name
##sys.argv[3] = length of reads
##sys.argv[4] = depth of coverage
# if __name__ == ' __main__':
# input = open(sys.argv[0],'r') #this will be uncommented later!
# output = open(sys.argv[1], 'w') ##this will be uncommented later
# lenreads = sys.argv[2]
# dc = sys.argv[3]
input = open('test.fasta', 'r')
#read in the fasta file
for record in SeqIO.parse (input, 'fasta'): 
    #print(record.seq)
    #print(record.id)
    identifiers = record.id
    strsequences = str(record.seq)
    sequences = list(record.seq)
    #print(identifiers)

##make reverse complement strand of sequences using BIoSeq
tobeRC = Seq(strsequences)
RC = tobeRC.reverse_complement()
RC = str(RC)
listRC = list(RC)
# print(type(RC))
# print(type(listRC))

def makeQS(listofsequences, outputfilename): 
#make list of random numbers between 0 and 9 for the quality score
    qs = []
    for nuc in range(len((listofsequences))):
        n = str(random.randint(0,9))
        qs.append(n)
    #print(qs)
    #print(len(qs)) length matches sequence list length
    listofsequences = ''.join(x for x in listofsequences)
    listofsequences = str(listofsequences)
    qs = ''.join(y for y in qs)
    #print(type(qs))
    #qs = str(qs)
    output = open(outputfilename, 'w')
    output.write(identifiers+'\n')
    output.write(listofsequences + '\n')
    output.write('+' + '\n')
    output.write(qs)
    output.close()

makeQS(sequences, identifiers+'.fastq')
makeQS(listRC, 'RC_'+identifiers+'.fastq')

print('See output files for fastq files')
# output = open('fakefastq.fastq', 'w')
# output.write(identifiers+'\n')
# output.write(sequences + '\n')
# output.write('+' + '\n')
# output.write(qs)
# output.close()
# print('see output file for output') #this kinda works but it could probs be modified a little bit

##if the above is going to be my output then I need to read in my fasta file and save the ids to a list and the sequences to a list and then iterate through them
##to get the quality line I am going to have to match/ make sure that the numpy value is between 0 and 9 so that it can match with the nucs in the sequence

