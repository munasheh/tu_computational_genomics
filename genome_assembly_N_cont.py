##import modules
from Bio import SeqIO
import sys
import numpy
import os

#command line arguments
# [1] = fast #file of assembled contigs
# [2] = x value for Nx #(usually 50)
# [3] = the actual size of the genome

l = sys.argv[3]

#fasta = open(sys.argv[1]) ##this wil be the name of the fasta  file
fasta = open(sys.argv[1],'r')

#make empyt list to hold the lengths of the sequences
seqList = []#this will be a list of lengths
tl = [] #this will be a list of all the sequences combined

#bigSeq = []#cheking total length

for record in SeqIO.parse (fasta, 'fasta'): 
    record = str(record.seq)
    #print(len(record))
    #print(type(record))
    tl.append(record)
    
#need to add everything in tl together
tl = ''.join(tl)
ntl = int(len(tl)) #this is the length of all the contigs

fasta1 = open('contigs.fa')
sequences = []
slio = []
for record in SeqIO.parse(fasta1, 'fasta'):
    nucs = str((record.seq))
    #print(len(nucs))
    sequences.append(nucs)

newlist =sorted(sequences,key=len)
newlist.reverse()
newlistLengths = [] 
for sequence in newlist:
    if len(sequence) > 0:
        z = len(sequence)
        newlistLengths.append(z)

nnlist = ''.join(newlist) #use this to do the index thing with
Nx = sys.argv[2]
Nx = int(Nx)
#Nx = int(input('Please enter the N value you wish to find:'))#change to command line sequence later -->argument2 
Nx = (Nx/100)
#print(Nx)

#Nx practice!
#print(type(Nx)) #this has to stay a float value or else it will round to 0
index = (ntl*Nx)
#print(index)
integerIndex = int(index)-1
#print(nnlist[integerIndex])##this works
#print(integerIndex)

length = 0 
for x in newlistLengths:
    length = length + x
    if length < integerIndex:
        next
    if length >= integerIndex:
        answer = x
        break
print('N-value:', x)