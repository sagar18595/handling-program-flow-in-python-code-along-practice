# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)
 
 
# Code starts here
first_inning_delivery = data['innings'][0]['1st innings']['deliveries']
ganguly_delivery = 0
player_match_runs = 0
player_match = data['info']['player_of_match'][0]
batsman_first_inning = []
batsman_six = {}
batsman_bowled = []
first_extras = 0
second_extras = 0

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
for rec in first_inning_delivery :
    for key,val in rec.items() :
        if val['batsman'] == 'SC Ganguly' :
            ganguly_delivery += 1
        if val['batsman'] == player_match :
            player_match_runs += val['runs']['batsman']
        batsman_first_inning.append(val['batsman'])
        if val['runs']['batsman'] == 6 :
            if val['batsman'] in batsman_six :
                batsman_six[val['batsman']] += 1
            else :
                batsman_six[val['batsman']] = 1
        first_extras += val['runs']['extras']


print ("deliveries faced by ganguly - ",ganguly_delivery)
#  Who was man of the match and how many runs did he scored ?

print ("player of match -",player_match, " and runs scored - ",player_match_runs)

#  Which batsman played in the first inning?
print (set(batsman_first_inning))

# Which batsman had the most no. of sixes in first inning ?
print(max(batsman_six, key = batsman_six.get))
print ("***"*20)
# Find the names of all players that got bowled out in the second innings.
second_inning_delivery = data['innings'][1]['2nd innings']['deliveries']
for rec1 in second_inning_delivery :
    for key1,val1 in rec1.items() :
        if 'wicket' in val1 and 'bowled' in val1['wicket']['kind'] :
            batsman_bowled.append(val1['batsman'])
        second_extras += val1['runs']['extras']

print(batsman_bowled)

# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
print (second_extras - first_extras)


# Code ends here


