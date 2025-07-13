# week 1 part 2 try #3

# write a python program that reads in a Fasta file with multiple sequences
# have python file report any potential open reading frames
# reading frames do not need to start with M but must end with stop codons
# there are three stop codons, TAA, TAG and TGA

#import modules
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

print('Week 1, Part 2')
print('This script counts the number of open reading frames and reports them')
print('Open Reading Frames are counted by distance between stop codons, instructions for assignment said that not all ORFs needed to start with M')

# ####open file and read in fasta sequences
# ##for record in SeqIO.parse('yeastMrna.fasta', 'fasta'):
# ##    print (record.id)
# ##    print (len(record.seq)) #checking length of original sequences to see if they are more than 60 nucleotides long
# ##    #return record.seq.reverse_complement()

##make fasta file of RC sequences to run next defition on
def make_RC_record(record):
    return SeqRecord(seq = record.seq.reverse_complement(),id = record.id, description = "reverse complement")

records = map(make_RC_record, SeqIO.parse('yeastMrna.fasta','fasta'))
SeqIO.write(records,'yeastMrnaRC.fasta', 'fasta')
print('Reverse Complement sequenes have been written to yeastMrna.fasta')

# ##tell python what the stop codons are
# stopcodons = ['TAA', 'TAG', 'TGA']


def makeListofOrf(file):
    frames = []
    for record in SeqIO.parse(file, 'fasta'):
        dna = str(record.seq)
        description = record.id
        frames.append([dna[i:i + 3] for i in range(0, len(dna), 3)])
        frames.append([dna[i:i + 3] for i in range(1, len(dna), 3)])
        frames.append([dna[i:i + 3] for i in range(2, len(dna), 3)])
        orfCount(description, frames)
        frame = []
    # print(frames[1])



def orfCount(description, frames):
    listOfOrf = list()
    count = 0
    for i in range(0, len(frames), 1):  # looping all the frames
        start = 0
        # looping each frame for start and stop codons
        while start < len(frames[i]):
            if frames[i][start] == "ATG" or frames[i][start] == "TTG" or frames[i][start] == "CTG" or frames[i][start] == "GTG":
                for stop in range(start+1, len(frames[i]), 1):
                    if frames[i][stop] == "TAA" or frames[i][stop] == "TAG" or frames[i][stop] == "TGA":
                        # retrieve the orf
                        # print(start)
                        # print(stop)
                        listOfOrf.append(frames[i][start:stop])
                        if stop - start > 59:
                            count = count + 1
                        # print(frames[i][stop])
                        # print(frames[i][start:stop+1])
                        start = stop+1  # avoiding multiple start codons
                        break
            start += 1
    print(str(description) + ": " + str(count)) #make a dictionary and then update the dictionary

print('Number of possible open reading frames in foward strand of mRNA:')
makeListofOrf('yeastMrna.fasta')
print('ok')
print ('Number of possible open reading frames in reverse complement strand of mRNA:')
makeListofOrf('yeastMrnaRC.fasta')
print('These are the open reading frames')

