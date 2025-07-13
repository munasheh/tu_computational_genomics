##write a python script to read a chromosome
##make a map of the mutations, insertions, deletions, translocations and inversions that are generted from a probability distrubution for each
##iutput fasta file of your simulated homologous chromosome

##import modules
from Bio import SeqIO ##this is to read in the og chromosome
import numpy as np
import random
import math
file = input('enter the name of the file you wish to make a homologous chromosome from: ')
file = open(file, 'r')
##read in chromosome from the venter chromosome jawn
#file = open('test.fasta', 'r')
for record in SeqIO.parse(file, 'fasta'): #debating if I should save thses to a dictionary or not :/
    #print('Orginal chromosome:' + '\n' + record.seq) this line isnt really needed but I will keep it to make sure that the file is read in properly
    identifier = record.id
    ogsequence = list(record.seq)
#print('index 31 of og sequence:' + ogsequence[31]) #testing to make sure that og sequence is ordered 
#print('length of original sequence: ' + str(len(ogsequence)))

#make an empty list for the numbers that are produced by the random number generator
subList = []
for nuc in range(len((ogsequence))):
    n = (random.random()*100)
    subList.append(n)

#print(type(ogsequence)) is a list and looks the way that I want it to 

#make a set of the nucleotides, making set becausue it doesnt have to be ordered
nucList = ['A','T','G','C'] #Possibly add a space to this? probably not tho
#print(nucList) #type is a set so this is correct. Need to get numpy to tie into this set

#trying the indexes again
def sub(ogsequence,subList): 
    for i in range(len(ogsequence)):
        if ogsequence[i] == 'A' and subList[i] < 5.7:
            ogsequence[i] = random.sample(nucList,1)
            #print (i,ogsequence[i],subList[i])
        if ogsequence[i] == 'T' and subList[i] < 6.8:
            ogsequence[i] = random.sample(nucList,1)
            #print (i,ogsequence[i],subList[i])
            return ogsequence
        if ogsequence[i] == 'C' and subList[i] < 11.4:
            ogsequence[i] = random.sample(nucList,1)
            return ogsequence
            #return i, subList[i]
        if ogsequence[i] == 'G' and subList[i] < 11.5:
            ogsequence[i] = random.sample(nucList,1)
            return ogsequence
            #return i, subList[i]
        # if subList[i] < 5.7:
        #     print(i, subList[i])
sub(ogsequence,subList)
indelList = [] #this was changed from sublist
for nuc in range(len((ogsequence))):
    n = (random.random()*100)
    indelList.append(n)

indelk = np.random.gamma(1.0231,5.9413)#these numbers came from a paper
#print('k:', indelk)

##definitions for indels
def insert(ogsequence, indelList):
    a = 0.53
    b = 1.69
    fk = (a * indelk) ** (-b)
    #print('insertation fk:', fk)
    for nuc in ogsequence:
        if nuc in indelList < fk:
            ogsequence[nuc] = random.sample(nucList,math.ceil(indelk))
            print( nuc, ogsequence[nuc])
insert(ogsequence, indelList)

def deletion(ogsequence, indelList):
    a = 0.48
    b = 1.51
    delfk = (a * indelk) ** (-b)
    #print('deletion fk:', delfk)
    for nuc in ogsequence:
        if nuc in indelList < delfk:
            ogsequence.pop(nuc)
            print( nuc, ogsequence[nuc])
deletion(ogsequence, indelList) 

#print(len(ogsequence))

output = open('homochromoutput.txt', 'w')
output.write(identifier+'\n')
output.write(str(ogsequence))
output.close()

print('see homochromoutput.txt for homologous chromosome')
