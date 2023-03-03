import PySimpleGUI as sg

# fonts = (
#     ('Courier New', 8, 'italic'),
#     ('Courier New', 20, 'italic'),
#     ('Courier New', 40, 'italic'),
#     ('Courier New', 60, 'italic'),
#     None,
# )

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
window = sg.Window("Demo", layout)

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Add to Radar":
        break
    if event == sg.WIN_CLOSED:
        break

window.close()

