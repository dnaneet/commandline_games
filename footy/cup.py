import numpy as np
import pandas as pd
import os
import time
import pdb


'''
Function definitions
'''
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
def football_match(ts, g, team_1_advance, team_2_advance, team_1_name, team_2_name):  
  team_1_score=np.array([0])
  team_2_score=np.array([0])
  added_time = np.random.randint(7) 
  for i in range(89 + added_time): #begin loop
    p = np.random.randint(nSamples)
    if(p>=ts):
        team_1_advance = np.append(team_1_advance,[1], axis=0)
        team_2_advance= np.append(team_2_advance,[0], axis=0)
    else:
        team_1_advance= np.append(team_1_advance,[0], axis=0)
        team_2_advance= np.append(team_2_advance,[1], axis=0)  
    #n=np.int(0.5*g + np.random.randint(5))
    n = g
    if(np.cumsum(team_1_advance[-n:])[-1]>=n):
        team_1_score = team_1_score + 1
    if(np.cumsum(team_2_advance[-n:])[-1]>=n):        
        team_2_score = team_2_score + 1 #end loop

  #score tallying  
  #pdb.set_trace()
  if(team_1_score >=7 or team_2_score >=7): 
    team_1_score = np.random.randint([2])
    team_2_score = np.random.randint([2])  
    
  if(team_1_score != team_2_score):
    print(team_1_name, ':', team_1_score, team_2_name, ':', team_2_score, file=f1)
    return print(team_1_name, ':', team_1_score, team_2_name, ':', team_2_score) #final scoreline is presented
  elif(team_1_score == team_2_score):
    while(team_1_score == team_2_score):
        team_1_score = np.random.randint([3])
        team_2_score = np.random.randint([3])
    print(team_1_name, ':', team_1_score, team_2_name, ':', team_2_score, '(p)', file=f1)    
    return print(team_1_name, ':', team_1_score, team_2_name, ':', team_2_score, '(p)') #final scoreline is presented

'''
Import full SPI data
'''

os.system('clear')
team_list = pd.read_csv('./spi_global_rankings.csv')
team_list['rank'] = team_list.index
#print(team_list.head(5))
print('SPI data imported')
time.sleep(1)


eps=0.001;

worst_defense_val = np.max(team_list['def'])
best_defense_val = np.min(team_list['def'])

worst_attack_val = np.min(team_list['off'])
best_attack_val = np.max(team_list['off'])

rank_best = np.min(team_list['spi'])
rank_worst = np.max(team_list['spi'])


'''
Knock-out cup simulation
'''

df = pd.read_csv('match_listing.csv')
print('\n\nList of matches imported')
time.sleep(1)
print('\nList of games:\n\n', df)

nGames = 1

f1=open('./scorecard.txt', 'w+')
for match in range(len(df)):
    print('\n\nThis is match day:',match+1)    
    team_1_name = df['team 1'].iloc[match]
    team_2_name = df['team 2'].iloc[match]
    
    team_1_dfx = float(np.abs(worst_defense_val - team_list['def'][team_list['name']== team_1_name])/worst_defense_val)
    team_1_atx = float(team_list['off'][team_list['name']== team_1_name]/best_attack_val)
    team_1_rank = int(team_list['rank'][team_list['name'] == team_1_name])
    team_1_advance = np.array([0])
    
    team_2_dfx = float(np.abs(worst_defense_val - team_list['def'][team_list['name']== team_2_name])/worst_defense_val)
    team_2_atx = float(team_list['off'][team_list['name']== team_2_name]/best_attack_val)
    team_2_rank = int(team_list['rank'][team_list['name'] == team_2_name])
    team_2_advance = np.array([0])
    #pdb.set_trace();
    print(team_1_name, 'vs',  team_2_name, '\n\n')
    print('\nThe whistle blows and the game starts!')
    time.sleep(1)
    strength_factor = nSamples/2000
    team_strength = 0.5*nSamples + strength_factor*delta(team_1_rank, team_2_rank)
    gp = np.int(7 - team_1_dfx - team_2_dfx + team_1_atx + team_2_atx);
    football_match(team_strength, gp, team_1_advance, team_2_advance, team_1_name, team_2_name)
    input("Press Enter to continue...\n\n")
    

#eof

