import gkeepapi
import constants
import src.IGDBIntegration as igdb

keep = gkeepapi.Keep()
keep.login(constants.GKEEP_USERNAME,constants.GKEEP_PASSWORD)

def getVideoGameListFromKeep():
    glist = keep.get(constants.GKEEP_NOTEID)
    gameList = glist.text.splitlines()
    return gameList

def formatGameEntry(game):
    # Check game entry release date amd store it
    releaseDate = igdb.getReleaseDate(game)
    print("releaseDate:", releaseDate)
    return game+" - "+releaseDate

def formatGameFromList(game):
    secondIndex = game.index('-')-1
    return game[2:secondIndex]

def checkListForEntryAndAppend(entry, gameList, GUIPopUp):
    appendGame = True
    for gameValue in gameList:
        game = formatGameFromList(gameValue)
        if entry in game:
            # Notify user entry already exists if game is within array
            appendGame = False
            GUIPopUp()
    newGameList = gameList
    if appendGame == True:
        print('Adding',entry,'to game list')
        newGameList.append(formatGameEntry(entry))
    return newGameList

def writeGameListToKeep(gameList):
    glist = keep.get(constants.GKEEP_NOTEID)
    idx = list(range(len(glist.items)))
    for game in idx:
        item = glist.items[0]
        item.delete()
    for game in gameList:
        glist.add(game.replace('☐','').strip(), False, gkeepapi.node.NewListItemPlacementValue.Bottom)
    keep.sync()
    
