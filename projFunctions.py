import requests as rq
import pandas as pd

urlTGD = 'https://thegameday.com/fantasy/football/dynasty/'

def ScrapingPlayersTGD():
    playerDict = {}
    df = pd.read_html(urlTGD)

    # This returns the first table which is our targetted table
    dfRanks = df[0]

    # Assigns values into player dict in the form 'Player': [RK, POSRK]
    for i in range(300):
        # NameEditor ensures each dict has the same str for each player's name
        name = NameEditor(dfRanks['Player'][i])
        ovrRank = dfRanks['RK'][i]
        posRank = dfRanks['POSRK'][i]
        # Stores in the structure of 'PlayerName': ('ovrRank','posRank')
        playerDict[name] = [ovrRank, posRank]
    
    return playerDict

urlPFF = 'https://www.pff.com/news/fantasy-football-2023-post-nfl-draft-dynasty-rankings'

def ScrapingPlayersPFF():
    playerDict = {}
    
    # Additional request code necessary for avoiding gateway error
    url = rq.get(urlPFF)
    df = pd.read_html(url.text)

    # This returns the first table which is our targetted table
    dfRanks = df[0]

    # Each of the cols are the playerName, overRank, and posRank respectively
    for i in range(299):
        # NameEditor ensures each dict has the same str for each player's name
        name = NameEditor(dfRanks[2][i+1])
        ovrRank = dfRanks[0][i+1]
        posRank = dfRanks[4][i+1]
        # Stores in the structure of 'PlayerName': ('ovrRank','posRank')
        playerDict[name] = [ovrRank, posRank]
    
    return playerDict  

# Used to standarize particular names that are different between the two dicts
def NameEditor(name):
    if ' Jr.' in name:
        return(name.replace(' Jr.', ''))
    elif ' II' in name:
        return(name.replace(' II', ''))
    elif 'D.K.' in name:
        return(name.replace('D.K.', 'DK'))
    elif 'Gabriel' in name:
        return(name.replace('Gabriel', 'Gabe'))
    elif 'Josh' in name:
        return(name.replace('Josh', 'Joshua'))
    elif 'K.J.' in name:
        return(name.replace('K.J.', 'KJ'))
    # If the names do not apply to any of the if statements keep it the same
    else:
        return name
    
# Used to troubleshoot and see the names not in both of the dicts respectively
def NameDictChecker(dict1, dict2):
    notFoundNames1 = []
    notFoundNames2 = []

    # If the name is not in the other dict put it into the notFoundNames arr
    for key in dict2:
        if key not in dict1:
            notFoundNames1.append(key)

    # If the name is not in the other dict put it into the notFoundNames arr
    for key in dict1:
        if key not in dict2:
            notFoundNames2.append(key)
    
    # Lengths of the two arrays extra names arr
    print(len(notFoundNames1), len(notFoundNames2))

    # Printing the two arrays to find which names are not in both dicts
    print(sorted(notFoundNames1))
    print(sorted(notFoundNames2))
    