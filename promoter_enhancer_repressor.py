##this is a practice file for the promoter/enhancer/repressor jawn for the week 7 assignment
##need to get the per stuff to be numbers that change from 0-9 depending on the mutation rate, they should also have their own distrubution
##import modules
import random
import numpy as np
import copy

##get random number btwn 0 and 9 for the 1st 3 indexes of the jawn
# per = random.randint(0,9)
# print(per)
# members = int(input('please enter the number of members of each generation: ')) #uncomment later
# #members = 10

def initialize_parent(members):
    parental = []#this will be the starting generation jawn 
    for j in range (members):
        g0 = []
        for i in range (0,5):
            per = random.randint(-9,9)
            g0.append(per)
        #print(g0)
        parental.append(g0)
    #print(parental)
    #print('This is what the different indexes are for each member of the generation:P:0, E:1, R:2, #:3, #:4')

    #making sure that I can access the indexes within the parental list
    ##this is making sure that there are actual items in the lists that I am making
    for h in parental:
        #print(h)
        h[3]= 1
        h[4]= 2
        #need to ensure that the numbers are integers for what I want to work to actually work 
        for z in h: 
            z = int(z)
        #print(type(z))
        #dnc stands for do not change
    print('g0:', parental)
    return parental

##need to figure out what the distrubutions will be and how they will influece the final 2 numbers in the script
    # for u in h:
    #     print(u)
#mr = float(input('please enter the mutation rate you would like to use: ')) #uncomment later
def next_generation(prev_gen,members, mr):
    parental = copy.deepcopy(prev_gen)
    new_mut = random.randint(-10,10)##changed this from the other script because the numbers were crazy
    #print(new_mut)
    app_nums = []
    for i in parental: 
        i[3] = 1
        i[4] = 2
    #need to have the mutaiton rate affect the per and then have the per affect the 4(3) and 5(4) positions
    for indvl in parental: 
        # for place in indvl: 
        mutnum = np.random.uniform(0,1)
        #print(mutnum)
        # new_mut = random.randint(0, members)
        if mr < mutnum:
            indvl[0] = indvl[0] - new_mut 
            indvl[1] = indvl[1] - new_mut
            indvl[2] = indvl[2] + new_mut
        # print('p'+ str(indvl[0]))

        app = indvl[0] + indvl[1] + indvl[2]
        app_nums.append(app)
        # print(app) ##this is how the per will apply to the other 2 values in the jawn
    #print('g1:',parental)
    #print('app_nums:', app_nums)
    # for item in app_nums:
    #     print(item)

    #mutation needs to occur after mating
    n = random.sample(parental, (random.randint(0,members)))
    #print('n', n) #this gives the values in a different order than what is what the parental list is in. 
    #print(len(n))
    len_n = int(len(n)) #works
    #print(type(n))
    #need to find where in the indexes of all the items in n
    mm = []

    for k in n:
        index_n = parental.index(k)
        mm.append(index_n)
        mut_person = parental[index_n]
        #print('person:', mut_person)
        if app_nums[index_n] == 0:
            mut_person[3] = mut_person[3]
            mut_person[4] = mut_person[4]
        if app_nums[index_n]%2 == 0:
            #print('x')this works
            if app_nums[index_n] > 0:
                mut_person[3] = random.randint(0, gens)
            if app_nums[index_n] < 0:
                mut_person[3] = mut_person[4]
        if app_nums[index_n]%2 != 0:
            if app_nums[index_n] > 0:
                mut_person[4] = random.randint(0, gens)
            if app_nums[index_n] < 0:
                mut_person[4] = mut_person[3]
    return parental

#members = int(members) #need to change the type from a string to an integer to be used further down the script. 
# print('members type',type(members))
#print(members)
#memlen= int(len(members))
# print(memlen)
gens = int(input('please enter the number of generations: '))
#gens = 10
assert 1 < gens
members = int(input('please enter the number of members of each generation: '))
#members = 10
mr = float(input('please enter the mutation rate you would like to use: '))
assert 1 > mr > 0

prev_gen = initialize_parent(members= members)
next_gen = prev_gen

for i in range(1, gens+1):
    next_gen = next_generation(prev_gen=prev_gen, members = members, mr = mr)

print(f'final: {next_gen}')


