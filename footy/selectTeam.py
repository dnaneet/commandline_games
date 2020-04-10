'''
Team selection
'''
import os
import time
import numpy as np

os.system('clear')
print('**********************')
print('Command line football')
print('**********************')
time.sleep(.2)

team_1_dfx = float(input("Please enter team-1's defensive capabilities (0-1): "))
team_1_atx = float(input("Please enter team-1's attacking capabilities (0-1): "))
#print("You entered " + str(team_1_dfx))

team_2_dfx = float(input("Please enter team-2's defensive capabilities (0-1): "))
team_2_atx = float(input("Please enter team-2's attacking capabilities (0-1): "))


team_1_rank = int(input("Please enter team-1's rank (1-20): "))
#print("You entered " + str(team_1_rank))

team_2_rank = int(input("Please enter team-2's rank (1-20): "))

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
