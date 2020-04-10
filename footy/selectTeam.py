'''
Team selection
'''
import os
import time
import numpy as np
np.set_printoptions(precision=2)
import pandas as pd

os.system('clear')
team_list = pd.read_csv('./spi_global_rankings.csv')
team_list['rank'] = team_list.index
#print(team_list.head(5))
#print(team_list.columns)

eps=0.001;

worst_defense_val = np.max(team_list['def'])
best_defense_val = np.min(team_list['def'])

worst_attack_val = np.min(team_list['off'])
best_attack_val = np.max(team_list['off'])

rank_best = np.min(team_list['spi'])
rank_worst = np.max(team_list['spi'])

team_1_name = input("Please enter team-1's name: ")
team_1_dfx = float(np.abs(worst_defense_val - team_list['def'][team_list['name']== team_1_name])/worst_defense_val)
team_1_atx = float(team_list['off'][team_list['name']== team_1_name]/best_attack_val)
team_1_rank = int(team_list['rank'][team_list['name'] == team_1_name])



team_2_name = input("Please enter team-2's name: ")
team_2_dfx = float(np.abs(worst_defense_val - team_list['def'][team_list['name']== team_2_name])/worst_defense_val)
team_2_atx = float(team_list['off'][team_list['name']== team_2_name]/best_attack_val)
team_2_rank = int(team_list['rank'][team_list['name'] == team_2_name])

print('\nAttributes of ', team_1_name)
print('Defense:', np.round(team_1_dfx,2))
print('Attack:', np.round(team_1_atx,2))
print('World Football Rank:', team_1_rank)
print('\n\n')

print('Attributes of ', team_2_name)
print('Defense:', np.round(team_2_dfx,2))
print('Attack:', np.round(team_2_atx,2))
print('World Football Rank:', team_2_rank)

class team_1:
  "this is the class for the home team"
  defensive_tendency = team_1_dfx
  attacking_tendency = team_1_atx
  rank = team_1_rank
  advance = np.array([0])
  
class team_2:
  "This is the class for the away team"
  defensive_tendency = team_2_dfx
  attacking_tendency = team_2_atx
  rank = team_2_rank
  advance = np.array([0])


#eof
