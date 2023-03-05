import string
import PySimpleGUI as sg
import src.GoogleKeepIntegration as gkeep

def initialize(appName):
    titleFontSize = 45
    labelFontSize = 25
    buttonFontSize = 20

    layout = [
        [sg.Text("Game Radar", font=('Courier New', titleFontSize, 'italic'), justification=("center"), pad=((0,0),(0,15)), tooltip=("Enter name of a Video Game"))],
        [
            sg.Text("Enter Name:", font=(labelFontSize), justification=("left"), pad=((0,0),(0,20))), 
            sg.Input("", pad=((0,0),(0,18)), tooltip=("Enter name of a Video Game"), size=(38,0))
        ], 
        [sg.Button("Add to Radar", font=(buttonFontSize), pad=((258,0),(0,5)))]
    ]
    window = sg.Window(appName, layout)

    def GUIPopUp():
        print('Entry already exists in game')
        sg.popup_auto_close('Entry already exists in Game Radar', auto_close_duration=(10))

    def has_numbers(inputString):
        return any(char.isdigit() for char in inputString)
            
    def sortGameList(gameList):
        gameListTop = []
        gameListMid = []
        gameListBot = []
        for game in gameList:
            gameDate = game.split("-")[1]
            if "Out" in gameDate:
                gameListTop.append(game)
            elif has_numbers(gameDate):
                gameListMid.append(game)
            else:
                gameListBot.append(game)
        gameListMid1 = []
        gamelistMid2 = []
        for game in gameListMid:
            date = game.split("-")[1]
            if len(date.split(" ")) > 2:
                gameListMid1.append(game)
            else:
                gamelistMid2.append(game)
        gameListMid1.sort(key=lambda x: x.split("-")[1].split(" ")[1])
        gamelistMid2.sort(key=lambda x: x.split("-")[1])
        gameListMid = gameListMid1 + gamelistMid2
        gameListTop.sort()
        gameListBot.sort()
        modifiedGameList = gameListTop + gameListMid + gameListBot
        return modifiedGameList

    while True:
        event, values = window.read()
        # User presses the button
        if event == "Add to Radar":
            userInput = string.capwords(values[0])
            print("You entered:", userInput)
            # Read google keep and return Array of games
            gkeepGameList = gkeep.getVideoGameListFromKeep()
            # Check Array for given value and add entry if game not found within array
            gameList = gkeep.checkListForEntryAndAppend(userInput, gkeepGameList, GUIPopUp)
            # Re-sort game list based on release date (already released at top while TBD at bottom)
            modifiedGameList= sortGameList(gameList)
            # Write Game List to GKeep
            gkeep.writeGameListToKeep(modifiedGameList)
        # End program if user closes window
        if event == sg.WIN_CLOSED:
            break

    window.close()

