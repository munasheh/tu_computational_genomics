##write a python program that will pull out sequences based on their barcode
##program should remove the barcode and leave the sequence
#turn in a folder with your program and ten files (one for each sequence)

##import modules
import random 


print('week 2 part 1')
print('This is a python program that will pull sequences from a fasta file using thie barcode. The program will remove the barcode and leave the sequence')
print('This program builds off of the program provided in class')

#program addbarcodes.py replaces the first ten bases with a barcode. 
##since these are a list they can be indexed
barcodes = ['ATGAGATCTT',
            'AGCTCATTTC',
            'TGAAAATCTT',
            'TATCCAGCCA',
            'AGGCAGGCAG',
            'CTTGTTACTA',
            'AAGGCACAAG',
            'TGCTCGCTGA',
            'GTACCGCCGT',
            'CCTCACCAGC']

#open files that will be written to at the end of this
##with open ('sequenceone.fq''w') as one, open ('sequencetwo.fq','w') as two, open('sequencethree.fq', 'w') as three, open ('sequencefour','w') as four, open('sequencefive','w') as five, open('sequencesix.fq','w') as six, open('sequenceseven.fq','w') as seven, open('sequenceeight.fq','w') as eight, open ('sequencenine.fq','w')as nine, open ('sequenceten.fq','w') as ten:
     ##create definition 

#bs is barcoded sequences
bs = input('Please enter the name of the file containing sequences. ')
#out = 'outputfile.txt'


fb = open(bs,"r")

while True:
    line = fb.readline()
    if len(line) ==0:
        break
    newseq = random.choice(barcodes)
    if newseq == barcodes[0]:
        fo = open('b1.fq','a')
    if newseq == barcodes [1]:
        fo = open('b2.fq', 'a')
    if newseq == barcodes [2]:
        fo = open('b3.fq','a')
    if newseq == barcodes [3]:
        fo = open ('b4.fq','a')
    if newseq == barcodes [4]:
        fo = open('b5.fq', 'a')
    if newseq == barcodes [5]:
        fo = open ('b6.fq', 'a')
    if newseq == barcodes [6]:
        fo = open('b7.fq', 'a')
    if newseq == barcodes [7]:
        fo = open('b8.fq', 'a')
    if newseq == barcodes [8]:
        fo = open('b9.fq','a')
    if newseq == barcodes [9]:
        fo = open('b10.fq', 'a')

    fo.write(line)
    sline = fb.readline()
    #newsline = sline.replace('ATGAGATCTT','')
    fo.write(sline)
    plus = fb.readline()
    qscore = fb.readline()
fb.close()
print('Finished! See files b1.fq, b2.fq, b3.fq, b4.fq, b5.fq, b6.fq, b7.fq, b8.fq, b9.fq and b10.fq for results')# finish this print statment