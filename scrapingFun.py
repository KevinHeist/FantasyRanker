import requests as rq
import pandas as pd

urlTGD = 'https://thegameday.com/fantasy/football/dynasty/'

def ScrapingPlayersTGD():
    playerDictTGD = {}
    df = pd.read_html(urlTGD)
    # This returns the first table which is our targetted table
    dfRanks = df[0]

    # Assigns values into player dict in the form 'Player': [RK, POSRK]
    for i in range(300):
        name = dfRanks['Player'][i]
        posRank = dfRanks['POSRK'][i]
        ovrRank = dfRanks['RK'][i]
        playerDictTGD[name] = [ovrRank, posRank]
    
    return playerDictTGD

urlFP = 'https://www.fantasypros.com/nfl/rankings/dynasty-overall.php'

def ScrapingPlayersFP():
    
