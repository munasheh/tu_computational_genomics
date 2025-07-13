##import modules
import Bio
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio import Entrez
import sys
from Bio.Blast import NCBIWWW
import random

##look up fasta sequence using the accession number
#myemail = 'munasheholloman@gmail.com'
myemail = str(input('please enter the email you would like NCBI to have: ' ))

sequence_id = 'NG_017013.2'
#sequence_id = str(input('please enter the NCBI accession number of the gene you are trying to find: '))

dbb = 'nucleotide'
##you can add an input statement later if you want to

#get fasta file of genes
initial_fasta = open('TP53.fasta','w')
myhandle = Entrez.efetch(db='nucleotide', id = sequence_id, rettype = 'fasta', email = 'munasheholloman@gmail.com')

initial_fasta.write(myhandle.read())
initial_fasta.close()

print('see TP53.fasta for fasta sequences for the genes used in this project')

#options for mutation: substitution, deletion, insertion 
def nonsynom (fasta):
    with open(fasta,'r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            #print(len(record.seq))
            options = ['sub']
            nuc_options = ['A','T','C','G']
            #mutation_type = random.choice(options)
            mutation_type = 'sub'
            print('mutation type', mutation_type)
            #options = ['A','T','G','C'] #options for substitution
            #print(options[3])
            seqlength = len(record.seq)
            sequence = list(record.seq)
            print('initial length of sequence: ', len(sequence))
            mutation_point = random.randint(0,seqlength)
            print('mutaton point:', mutation_point)
            print(sequence[mutation_point])
            #print(type(sequence)) this is a list
            ##resoning for following for loops: deletion and insertion can occur with any number of nucleotides, subsitution mutation is only for one nucleotide
            replacement = random.choice(nuc_options)
            sequence[mutation_point] = replacement
            print(replacement)
        # if mutation_type == 'del':
        #     # del_num = random.randint(0,len(sequence))
        #     # for num in range((del_num)-1):
        #     del(sequence[mutation_point])
        #     #sequence = ''.join(sequencelist)
        # if mutation_type == 'ins':
        #     ins_num = random.randint(0,len(sequence))#this should give you the number of items added
        #     for num in range(ins_num):
        #         sequence.insert(mutation_point, random.choice(nuc_options))
            print('mutation_point2:',sequence[mutation_point])
        print('final length', len(sequence))
        
        newseq = ''
        for ele in sequence:
            newseq += ele
    
    #print(len(newseq))matches previous sequence length 

    #need to write to a file and then make five files
    output = str(input('please enter the name of the output file you would like to use: '))
    f = open(output, 'w')
    f.write('>'+ input('please enter the sequence id you would like to use: ')+'\n')
    f.write(newseq)
    f.close
    

    #return sequence

                
# def listtoString(list_item):
#     str1 = ''
#     for ele in list_item:
#         str1 += ele
                    


        

TP53 = 'TP53.fasta'
nonsynom(TP53)

