import gkeepapi
import constants

keep = gkeepapi.Keep()
keep.login(constants.GKEEP_USERNAME,constants.GKEEP_PASSWORD)

def getVideoGameListFromKeep():
    gnote = keep.get(constants.GKEEP_NOTEID)
    gameList = gnote.text.splitlines()
    return gameList

def formatGameEntry(game, releaseDate):
    if "" in releaseDate:
        releaseDate = "TBD"
    # print("releaseDate:", releaseDate)
    return "☐ "+game+" - "+releaseDate

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
        newGameList.append(formatGameEntry(entry, ""))
    return newGameList