'''
Commandline Footy version 1.0
'''
import numpy as np
import os
import time
import matplotlib.pyplot as plt
import pdb

import selectTeam

nSamples = 4000; #This should be defined as a global variable

'''
Calculation of relative rank:
Strength of team 1 wrt team 2
If team-1 has a greater rank than team-2,
team-1 has a greater probability of winning
against team-2
'''
def relative_rank(t1r, t2r):
    if(t1r < t2r):
        return np.round(t2r/t1r)
    else:
        return np.round(t1r/t2r) 

'''
The delta value decides the strength of one 
team against the other.  
'''

def delta(t1r, t2r):
    if(t1r < t2r):
        return -np.round(t2r/t1r) #team-1 is stronger than team-2
    else:
        return np.round(t1r/t2r) #team-2 is stronger than team-1

'''
football match simulator
'''
def football_match(ts, g):
  team_1_score=np.array([0])
  team_2_score=np.array([0])
  added_time = np.random.randint(7) 
  for i in range(89 + added_time): #begin loop
    p = np.random.randint(nSamples)
    if(p>=ts):
        selectTeam.team_1.advance= np.append(selectTeam.team_1.advance,[1], axis=0)
        selectTeam.team_2.advance= np.append(selectTeam.team_2.advance,[0], axis=0)
    else:
        selectTeam.team_1.advance= np.append(selectTeam.team_1.advance,[0], axis=0)
        selectTeam.team_2.advance= np.append(selectTeam.team_2.advance,[1], axis=0)  
    #n=np.int(0.5*g + np.random.randint(5))
    n = g
    if(np.cumsum(selectTeam.team_1.advance[-n:])[-1]>=n):
        team_1_score = team_1_score + 1
    if(np.cumsum(selectTeam.team_2.advance[-n:])[-1]>=n):        
        team_2_score = team_2_score + 1 #end loop

  #score tallying  
  #pdb.set_trace()
  if(team_1_score >=7 or team_2_score >=7): 
    team_1_score = np.random.randint([2])
    team_2_score = np.random.randint([2])
  
  return print(team_1_score, team_2_score) #final scoreline is presented


'''
Simulate one-off or tournament 
between two teams
'''

nGames = int(input("How many games in the tournament? (minimum 1) "))
if(nGames == 1):
    #strength_factor = np.round(np.max(selectTeam.team_1.rank, selectTeam.team_2.rank)/np.min(selectTeam.team_1.rank,       selectTeam.team_2.rank))
    strength_factor = nSamples/100
    #print(delta(selectTeam.team_1.rank, selectTeam.team_2.rank))
    team_strength = 0.5*nSamples + strength_factor*delta(selectTeam.team_1.rank, selectTeam.team_2.rank); #relative rank  
    #gp = np.int32(elative_rank(selectTeam.team_1.rank, selectTeam.team_2.rank)); #goal potential
    gp = np.int(7 - selectTeam.team_1.defensive_tendency - selectTeam.team_2.defensive_tendency + selectTeam.team_1.attacking_tendency + selectTeam.team_2.attacking_tendency);
    #print('--------------')
    #print('Team strength: ', team_strength)
    #print('\n')
    #print('Goal potential: ', gp)
    #print('--------------')
    football_match(team_strength, gp)   
else:
    strength_factor = nSamples/100
    #pdb.set_trace()
    #print(delta(selectTeam.team_1.rank, selectTeam.team_2.rank))
    team_strength = 0.5*nSamples + strength_factor*delta(selectTeam.team_1.rank, selectTeam.team_2.rank); #relative rank  
    #gp = np.int32(relative_rank(selectTeam.team_1.rank, selectTeam.team_2.rank)); #goal potential
    gp = np.int(7 - selectTeam.team_1.defensive_tendency - selectTeam.team_2.defensive_tendency + selectTeam.team_1.attacking_tendency + selectTeam.team_2.attacking_tendency);
    #print('--------------')
    #print('Team strength: ', team_strength)
    #print('\n')
    #print('Goal potential: ', gp)
    #print('--------------')
    for i in range(nGames):
        football_match(team_strength, gp)       
#eof
