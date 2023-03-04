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

    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Add to Radar":
            print("You entered:", values[0])
            # Read google keep and return Array of games
            gameList = gkeep.getVideoGameListFromKeep()
            print("gameList:", gameList)
            # Check Array for given value
            # Add entry if game not found within array
            # Notify user entry already exists if game is within array
        if event == sg.WIN_CLOSED:
            break

    window.close()

