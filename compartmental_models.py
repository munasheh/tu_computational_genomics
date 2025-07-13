##import modules
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

N = int(input('please enter the population size, this program works best with low population sizes: '))
#N = 1000
I = int(input('Please enter the number of infectious individuals: '))
#I = 20
assert N > I

#Determine if there is a difference between recovered and death 
RorD = input('is there are a difference between the recovered and dead individuals in this exercise? ').lower()
if RorD == 'yes':
    D = int(input('please enter the number of deceased individuals '))
    R = int(input('please enter the number of individuals who have recovered '))
    assert D,R < N
    gamma = int(input('on average how long does it take an individual to recover (days)?This will be gamma '))
    assert gamma >0
    gamma = 1/gamma
    mu = int(input('on average, how long does it take a person to die from this disease (days)? This will be mu '))
    assert mu > 0
    mu = 1/mu
    float(mu)
    #mu = 'Not Applicable'
if RorD == 'no':
    R_D = int(input('please enter the number of people who have recovered/died: '))
    assert N > R_D
    gamma = float(input('please enter the recovery/death rate: '))
    assert 1 > gamma >0
    mu = 'Not Applicable, gamma will serve as the recovery/death rate'
if RorD == 'yes':
    S = N - I - (R+D)
if RorD == 'no':
    S = N - I - R_D 

#determine if there is long lasting immunity
LL = input('Does this disease cause long lasting immunity? ').lower() #this is implied with the original SIR model

#determine if there is a vaccine
V = input('Is there a vaccine for this disease? ').lower()
if V == 'yes':
    #V_num = int(input('Please enter the number of vaccinated individuals'))
    vac_rate = float(input('pleae enter the rate of vaccination : '))
    #V_num = vac_rate*N
    assert 1 > vac_rate > 0
    V_num = (vac_rate*N)
    round(V_num)
    assert V_num < N
    RorD = 'no'
    R_D = R+D
if V == 'no':
    vac_rate = 0
    V_num = vac_rate*N

#These are the rates:
beta = float(input('please input the contact rate: '))
print('These are the rates that you have inputted thus far: ')
# beta = float(input('please input the contact rate: '))
assert 0< beta< 1
print('the contact rate is', beta)
if RorD =='yes':
    print('the recovery rate is', gamma)
#if RorD =='yes' and RRD == 'deceased':
    print('the mortality rate is', mu) #both of these need to be defined if RRd is yes
if RorD  == 'no':
    print('the recovery/death rate is', gamma)
if V == 'yes':
    print('the rate of vaccination is ', vac_rate)
    print('the number of vaccinated individuals is ', V_num)

#make the timespace plot for the final figure
t = np.linspace(0,180,180)
#getting the y values for the definitions and loops (y)
if RorD == 'no' and LL == 'yes' and V == 'no':
    y0 =S,I,R_D
    y = S,I,R_D
#SIS model
if RorD == 'no' and LL == 'no' and V =='no':
    y0 = S,I
    y = S,I
#SIRD model
if RorD =='yes' and LL =='yes' and V == 'no':
    y0 = S,I,R,D
    y = S,I,R,D
#SIRV model, this will need to have two different things for the y and y0
if RorD == 'no' and LL == 'yes' or LL == 'no' and V == 'yes':
    y0 = S,I,R_D
    y = S,I,R_D
##all of the models that I have used are going to be in one definition and seperated by if/and statements
def SIR(y,t,N,beta, gamma, mu, vac_rate):
    '''this function determines which model will be used given the inputted information'''
    #this should be the classic SIR model, where recovered = removed = death
    if RorD == 'no' and LL == 'yes' and V == 'no':
        #print('We will be using the SIR model') this prints to the screen multiple times, idk why
        S,I,R_D = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt #3 compartments
    if RorD =='no' and LL == 'no' and V =='no':
    #this is the SIS model because there is no long lasting immunity
        #print('We will be using the SIS model becasue there is no long lasting immunity.')
        S,I= y
        dSdt = ((-beta*S*I)/N) + (gamma*I)
        dIdt = ((beta*S*I)/N)-(gamma*I)
        return dSdt, dIdt #2 compartments
    if RorD == 'yes' and LL == 'yes' and V == 'no':
        S,I,R,D= y #could also include D here, idk yet
        dSdt = (-beta*I*S)/N
        dIdt = ((beta*I*S)/N)-(gamma*I)- (mu*I)
        dRdt = gamma*I
        dDdt = mu*I
        return dSdt, dIdt, dRdt, dDdt #4 compartments
    if RorD =='no' and LL == 'yes' and V == 'yes':
        #print('We will be using the SIRV model because there is a vaccine avalible.')
        #this is if there is a vaccine avalible, This is the SIRV model
        S,I,R_D = y
        dSdt = (((beta*(t))*I*S)/N)-((vac_rate*t)*S)
        dIdt = (((beta*(t))*I*S)/N)- ((gamma*t)*(I))
        dRdt = (gamma*t)*I
        dVdt = (vac_rate*t)*S
        return dSdt, dIdt, dRdt, dVdt #4 compartments

def SIR2(y,t,N,beta, gamma, mu, vac_rate):
    '''this function is the same as SIR but is used with odeint to solve the equations'''
    #this should be the classic SIR model, where recovered = removed = death
    if RorD == 'no' and LL == 'yes' and V == 'no':
        #print('We will be using the SIR model') this prints to the screen multiple times, idk why
        S,I,R_D = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt #3 compartments
    if RorD =='no' and LL == 'no' and V =='no':
    #this is the SIS model because there is no long lasting immunity
        #print('We will be using the SIS model becasue there is no long lasting immunity.')
        S,I= y
        dSdt = ((-beta*S*I)/N) + (gamma*I)
        dIdt = ((beta*S*I)/N)-(gamma*I)
        return dSdt, dIdt #2 compartments
    if RorD == 'yes' and LL == 'yes' and V == 'no':
        S,I,R,D= y 
        dSdt = (-beta*I*S)/N
        dIdt = ((beta*I*S)/N)-(gamma*I)- (mu*I)
        dRdt = gamma*I
        dDdt = mu*I
        return dSdt, dIdt, dRdt, dDdt #4 compartments
    if RorD =='no' and LL == 'yes' and V == 'yes':
        #print('We will be using the SIRV model because there is a vaccine avalible.')
        #this is if there is a vaccine avalible, This is the SIRV model
        S,I,R_D,V_num = y
        dSdt = (((beta*(t))*I*S)/N)-((vac_rate*t)*S)
        dIdt = (((beta*(t))*I*S)/N)- ((gamma*t)*(I))
        dRdt = (gamma*t)*I
        dVdt = (vac_rate*t)*S
        return dSdt, dIdt, dRdt, dVdt #4 compartments

##get the compartments, this is really the amount of items that are returned
SIR(y, t, N, beta, gamma, mu, vac_rate)  #This works with the above line as SIR
compartments = len(SIR(y, t, N, beta, gamma, mu, vac_rate))#trying to see if I can somehow get the number of compartments out of this thing
print('this model has', compartments, 'compartments') #this is working now, need to write something that seperates the histograms into compartments, should be easy 
int(compartments)

if RorD == 'no' and V == 'yes':
    y0 = S,I,R_D,V_num

# Integrate the SIR equations over the time grid, t.
def SIR3(y,t,k):
    '''this function is the same as SIR but is used with odeint to solve the equations'''
    #this should be the classic SIR model, where recovered = removed = death
    if RorD == 'no' and LL == 'yes' and V == 'no':
        #print('We will be using the SIR model') this prints to the screen multiple times, idk why
        S,I,R_D = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt #3 compartments
    if RorD =='no' and LL == 'no' and V =='no':
    #this is the SIS model because there is no long lasting immunity
        #print('We will be using the SIS model becasue there is no long lasting immunity.')
        S,I= y
        dSdt = ((-beta*S*I)/N) + (gamma*I)
        dIdt = ((beta*S*I)/N)-(gamma*I)
        return dSdt, dIdt #2 compartments
    if RorD == 'yes' and LL == 'yes' and V == 'no':
        S,I,R,D= y #could also include D here, idk yet
        dSdt = (-beta*I*S)/N
        dIdt = ((beta*I*S)/N)-(gamma*I)- (mu*I)
        dRdt = gamma*I
        dDdt = mu*I
        return dSdt, dIdt, dRdt, dDdt #4 compartments
    if RorD =='no' and LL == 'yes' and V == 'yes':
        #print('We will be using the SIRV model because there is a vaccine avalible.')
        #this is if there is a vaccine avalible, This is the SIRV model
        S,I,R_D,V_num = y
        dSdt = (((beta*(t))*I*S)/N)-((vac_rate*t)*S)
        dIdt = (((beta*(t))*I*S)/N)- ((gamma*t)*(I))
        dRdt = (gamma*t)*I
        dVdt = (vac_rate*t)*S
        return dSdt, dIdt, dRdt, dVdt #4 compartments
if RorD == 'no' and LL == 'yes' and V == 'no':
    k = N,beta,gamma
#SIS model
if RorD == 'no' and LL == 'no' and V =='no':
    k = N,beta,gamma
#SIRD model
if RorD =='yes' and LL =='yes' and V == 'no':
    k = N,beta,gamma,mu
#SIRV model, this will need to have two different things for the y and y0
if RorD == 'no' and LL == 'yes' or LL == 'no' and V == 'yes':
    k = N,beta,gamma,vac_rate

ret = odeint(SIR3, y0, t, args=(k,))
print('made_ret')

# #need to get the rets to match up to y0 and y for the histogram to form 
if RorD == 'no' and LL == 'yes' and V == 'no':
    S,I,R_D = ret.T
#SIS model
if RorD == 'no' and LL == 'no' and V =='no':
    S,I = ret.T
#SIRD model
if RorD =='yes' and LL =='yes' and V == 'no':
    S,I,R,D = ret.T
#SIRV model
if RorD == 'no' and LL == 'yes' and V == 'yes':
    S,I,R_D,V_num = ret.T

# u = int(input('please enter the number that you want as the upper range on the graph'))
u = N+100
x = u/1000
# x = N+100
def histogram(compartments):
    #print('HISTO IS STARTING') #keep this for testing
    '''used to create the histograms for each model, there are 3 categories of histograms, 2,3 and 4(2)'''
    if compartments == 3:
        #this is the traditional SIR model
        fig = plt.figure(facecolor='w')
        plt.suptitle('SIR Model')
        ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
        ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
        ax.plot(t, R_D/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
        ax.set_xlabel('Time /days')
        ax.set_ylabel('Number (1000s)')
        ax.set_ylim(0,x)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(b=True, which='major', c='w', lw=2, ls='-')
        legend = ax.legend()
        legend.get_frame().set_alpha(0.5)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        plt.show()
    if compartments == 2:
        fig = plt.figure(facecolor='w')
        plt.suptitle('SIS model')
        ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
        ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
        ax.set_xlabel('Time /days')
        ax.set_ylabel('Number (1000s)')
        ax.set_ylim(0,x)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(visible=True, which='major', c='w', lw=2, ls='-')
        legend = ax.legend()
        legend.get_frame().set_alpha(0.5)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        plt.show()
    if compartments == 4 and V == 'yes':
        #SIRV model histo
        print('trying to make histogram')
        fig = plt.figure(facecolor='w')
        plt.suptitle('SIRV Model')
        ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
        ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
        ax.plot(t, R_D/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
        ax.plot(t, V_num/1000, 'purple', alpha=0.5, lw=2, label='Vaccinated')
        ax.set_xlabel('Time /days')
        ax.set_ylabel('Number (1000s)')
        ax.set_ylim(0,x)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(visible=True, which='major', c='w', lw=2, ls='-')
        legend = ax.legend()
        legend.get_frame().set_alpha(0.5)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        plt.show()
    if compartments == 4 and RorD == 'yes':#need to see if either of the 4 compartment things work
        #SIRD model
        fig = plt.figure(facecolor='w')
        plt.suptitle('SIRD Model')
        ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
        ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
        ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
        ax.plot(t, D/1000, 'yellow', alpha=0.5, lw=2, label='Deceased')
        ax.set_xlabel('Time /days')
        ax.set_ylabel('Number (1000s)')
        ax.set_ylim(0,x)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(visible=True, which='major', c='w', lw=2, ls='-')
        legend = ax.legend()
        legend.get_frame().set_alpha(0.5)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        plt.show()
    print('see histogram file for relevant histogram!')

#call histogram function 
histogram(compartments) #this should make the histogram that is relavent to each model


print('THE END')



