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

    while True:
        event, values = window.read()
        # User presses the button
        if event == "Add to Radar":
            userInput = string.capwords(values[0])
            print("You entered:", userInput)
            # Read google keep and return Array of games
            gkeepGameList = gkeep.getVideoGameListFromKeep()
            # print("gkeepGameList:", gkeepGameList)
            # Check Array for given value and add entry if game not found within array
            gameList = gkeep.checkListForEntryAndAppend(userInput, gkeepGameList, GUIPopUp)
            print("gameList:", gameList)
        # End program if user closes window
        if event == sg.WIN_CLOSED:
            break

    window.close()

