##import modules
import numpy as np
import random

##get input from the users
#get the number of people in each generation (N)
N = int(input('please enter the number of individuals in each generation: '))
assert N>1
#get the mutation rate from the user
mr = float(input('please enter the mutation rate:' ))
assert 1 > mr > 0
#get the number of generations (gens)
gens = int(input('please enter the number of generations: '))
assert gens > 1
#make a random number that the mr has to be below for the mutation to occur
#mutnum = np.random.uniform(0,1)
#print(mutnum)

#make a list of the children in each generation
# kids = []
# for i in range(N):
#    pair = [1,2]
#    kids.append(pair) 

#print(kids) this works
for i in range(gens):
    g0 = []
    options = []
    gen1 = []
    for i in range(N):
        pair = [1,2]
        g0.append(pair)
    for z in g0:
        kids = random.sample(g0, k = 2)
        for h in kids:
            g2 = random.sample(h, k =1)
    #print(i) #this works and prints N-1
    for z in g0:
        g1 = random.sample(g0, k =2)
        for h in g1:
            g2 = random.sample(h, k =1) 
            options.append(g2)
    for i in range(N):
        child = (options[i]), (options[i+1])
        gen1.append(child)
        #print(gen1)
        change1 = random.randint(0,len(g0))-1 ## this gives you the person in the list to apply the mutation rate to
        change2 = random.randint(1,len(child)) - 1
    mutnum = np.random.uniform(0,1)
    if mr < mutnum:
        mut_person = gen1[change1]
        mut_site = mut_person[change2]
        mut_site[0] = random.randint(0,N)
        #print(gen1)
    #parent = gen1

print('the two alleles for the G0 will be 1 and 2, each item in the following lists indicates an individual in the population')
print('G0:', g0)
#print('options',options)
print('final generation', gen1)
