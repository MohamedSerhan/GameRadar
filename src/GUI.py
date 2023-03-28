import re
import string
import PySimpleGUI as sg
import src.GoogleKeepIntegration as gkeep

def GUIPopUp():
    print('Entry already exists in game')
    sg.popup_auto_close('This game is already in your Game Radar', auto_close_duration=(10))

def has_numbers_check(input_string):
    return any(char.isdigit() for char in input_string)

def sort_game_list(game_list):
    game_list_top = []
    game_list_mid = []
    game_list_bot = []

    # List comprehension
    [game_list_top.append(game) if "Out" in game.split("-")[1] else 
     (game_list_mid.append(game) if has_numbers_check(game.split("-")[1]) 
      else game_list_bot.append(game)) for game in game_list]

    game_list_mid1 = []
    game_list_mid2 = []

    # List comprehension
    [game_list_mid1.append(game) if len(game.split("-")[1].split(" ")) > 2 
     else game_list_mid2.append(game) for game in game_list_mid]

    game_list_mid1.sort(key=lambda x: x.split("-")[1].split(" ")[1])
    game_list_mid2.sort(key=lambda x: x.split("-")[1])
    game_list_mid = game_list_mid1 + game_list_mid2
    game_list_top.sort()
    game_list_bot.sort()
    modified_game_list = game_list_top + game_list_mid + game_list_bot
    return modified_game_list

def initialize(appName):
    title_font_size = 45
    label_font_size = 25
    button_font_size = 20

    layout = [
        [sg.Text("Game Radar", font=('Courier New', title_font_size, 'italic'), justification=("center"), pad=((0,0),(0,15)), tooltip=("Enter name of a Video Game"))],
        [
            sg.Text("Enter Name:", font=(label_font_size), justification=("left"), pad=((0,0),(0,20))), 
            sg.Input("", pad=((0,0),(0,18)), tooltip=("Enter name of a Video Game"), size=(38,0))
        ], 
        [sg.Button("Add to Radar", font=(button_font_size), pad=((258,0),(0,5)))],
    ]
    window = sg.Window(appName, layout)

    while True:
        event, values = window.read()

        # User presses the button
        if event == "Add to Radar":
            user_input = values[0]
            if not re.match("^[a-zA-Z\s]+$", user_input):
                sg.popup("Invalid input. Please enter a valid name (letters and spaces only).")
                continue
            user_input = string.capwords(user_input)
            print("You entered:", user_input)

            # Read google keep and return Array of games
            try:
                gkeep_game_list = gkeep.get_video_game_list_from_keep()
            except Exception as e:
                sg.popup("Error reading Google Keep: " + str(e))
                continue
            
            # Check Array for given value and add entry if game not found within array
            game_list = gkeep.check_list_for_entry_and_append(user_input, gkeep_game_list, GUIPopUp)

            # Re-sort game list based on release date (already released at top while TBD at bottom)
            modified_game_list = sort_game_list(game_list)

            # Write Game List to GKeep
            try:
                gkeep.write_game_list_to_keep(modified_game_list)
            except Exception as e:
                sg.popup("Error writing to Google Keep: " + str(e))
                continue

        # End program if user closes window
        if event == sg.WIN_CLOSED:
            break

    window.close()
