##write a script to download test data for the final project
##week7assignment

##inport modules
import Bio
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio import Entrez
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo.Applications import PhymlCommandline

##download NCBI records using Entrez

#Accession numbers ---> 
myemail = input('please enter your email address: ')
# idlist = ['AJ536470','AJ536476','AJ536469','AJ536467','AJ536468','AJ536475','AJ536471',
#           'AJ536472','AJ536473', 'AJ536479', 'AJ536481', 'AJ536478',
#           'AJ536480', 'AJ536483'] #try and get this to be an inputted list of accesion numbers?
idlist = input('Enter the accession number of whatever you are trying to get from NCBI: ')
# list(idlist)
# print(type)
print(idlist)

##file handle where retrives records will be saved
outfilename = input('name of the file that you would like to be written to:')
myfafile = open(outfilename, 'w')
dbb = input('specify protein or nucleotide(all lowercase): ')

##make a call to NCBI for a record in fasta format
myhandle = Entrez.efetch(db=dbb, id = idlist, rettype = 'fasta', email = myemail)

##print the lengths of the sequences to the screen
sl = []
for sr in SeqIO.parse(myhandle, 'fasta'):
    print(sr.id)
    print(sr.description)
    print(sr.seq)
    output = (sr.id), (sr.seq)
    sl.append(output)
# for i in range(len(sl)):
#     print(sl[i])

##make a call to NCBI for a record in fasta format
myhandle = Entrez.efetch(db=dbb, id = idlist, rettype = 'fasta', email = myemail)

##write to the file and close the file
myfafile.write(myhandle.read())
myfafile.close()
fetchedlist = ('Entrez.efetch return written to {}'.format(outfilename))
print(fetchedlist)