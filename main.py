from projFunctions import *

# Stores in the structure of 'PlayerName': ('ovrRank','posRank')
playerDictTGD = ScrapingPlayersTGD()
playerDictPFF = ScrapingPlayersPFF()

### Checks which names are not found in both dicts
# NameDictChecker(playerDictTGD, playerDictPFF)

### Synthesize the two dicts together, put all of the players into 1 dict and have the two sites' rankings
### within the same dict. Then average the two scores together. If one is in one dict and not in the other,
### leave the avg ranking as a combination of the two numbers (284/300+). Could also just assume 310 or 
### something. Then in the end make my own adjusted rankings using the two sites. Don't forget there is 
### positions in the posRank

# playerDict['player'][1] gives you the pos rank [0] the ovr rank

fullPlayerDict = {}

fullPlayerDict = CombineFunction(playerDictTGD, playerDictPFF, fullPlayerDict)

# player [[rank1, rank2], [posRank1, posRank2]]
# some might not have two rankings meaning there is only collectively in both the dicts
print(fullPlayerDict)