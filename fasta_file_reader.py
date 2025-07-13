##write a program that reads in a fasta file
##determine if the fasta file contains DNA, mRNa or protien sequence
##counts all the bases of the different types
##reports the base counts
##reports the percentage of unambiguous bases
##can handle ambigous bases as part of the file
##reports GC content or amino acid sequences 

#write a program that reads in a fasta file
print ('Week 1, Part 1')
f=open('Dromel.fasta','r')
k= f.readlines()
#print(k)

#determine if the file contains DNA, RNA, or Protein Sequences
datalines=k[1:]
#print(datalines) this was to determine if the first line was erased
'''erased the first line so that I can loop through the sequence to see if there are any U's or protien letters
and so that I can join the strings together easier'''

##this is to join all the strings together, could possibly be done before line 15, idk yet
x=''
for d in datalines:
    x=x+d
##find a way to get rid of all the spaces in the file here, I think that is what is giving the high number of total bases (tb)
#print(x)

##counts all the bases of different types
a= x.count("G")
b = x.count('C')
c = x.count('A')
d = x.count('T')
e = x.count('U')
f = x.count('')

# e = x.count('')
# print(e) this was me checking to see what else could be in the file

#reports the base counts
print('Number of Guanines:', a)
print('Number of Cytosines:',b)
print('Number of Adenines:', c)
print('Number of Thymines:', d)
print ('Number or Uracils:',e)

#reports the percentage of unambigous bases
'''first find the number of unambigous bases'''
#print('total number of bases:', e)
#tub is the total number of unambigous bases
tub = a+b+c+d
#print(tub) checking to see if this is correct
tb=len(x) ##this number is wrong, figure out what is going on
#print(tb) checking to see if this is correct
pub= tub/tb
pub = pub*100
#print(pub)
print('Percentage of unambigous bases:', pub,'%')

#reports GC content
'''find total number of G and C's in sequence
then find the GC Content'''
gc = b+a
print('Number of Guanines and Cytosines in Fasta file:', gc)
gc = gc/tb
gc = gc*100
print('GC Content:', gc,'%')

