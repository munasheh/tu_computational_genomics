'''write a python script to read in your fasta file and identify orthologs using blastx
for this assignment use mouse if your analysis is in humans
have your program create a table(csv or tsv file) with headings of gene ids, orthoolog NCBI gene ids and the model species gene accession number
also have the program make a list of model species ortholog gene ids seperated by a comma
'''

##import modules
import Bio
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio import Entrez
import sys
from Bio.Blast import NCBIWWW
my_email = input('please enter the email associated with Entrez and NCBIWW: ')

#look up fasta using accession number


#idlist =['NG_017013.2','NG_007462.1','NG_007726.3','NG_008732.1']
idlist = ['NG_017013.2','NG_007462.1']
#idlist = list(input('please input the accession numbers of the files you would like to use'))
dbb = 'nucleotide'

#get fasta file of genes, I am not sure this is necessary 
initial_fasta = open('original_genes.fasta','w')
myhandle = Entrez.efetch(db=dbb, id = idlist, rettype = 'fasta', email = my_email)

initial_fasta.write(myhandle.read())
initial_fasta.close()

#below may not be neccessary tbh
print('see initial_genes.fasta for fasta sequences for the genes used in this project')
og_genes = open('original_genes.fasta','r')
for record in SeqIO.parse(og_genes, 'fasta'):
    print(record.id)

#these should be the names of the coulumn heads, they should be added to the pandas datafram after they are  made
gene_ids = []
ortholog_gene_id = []
model_species_accession_number = []
#possibly add the items to a pandas datafram after the jawn has run.
for item in idlist:
    blast_handle = NCBIWWW.qblast("blastx", "nr", item , entrez_query="txid10090[ORGN]", ncbi_gi = 'True')
    print(item)
