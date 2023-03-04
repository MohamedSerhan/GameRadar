import gkeepapi

keep = gkeepapi.Keep()
# Change to ENV vars
keep.login('user', 'pass')

# note = keep.createNote('Todo', 'Eat breakfast')
# note.pinned = True
# note.color = gkeepapi.node.ColorValue.Red
# keep.sync()

def getVideoGameListFromKeep():
    gnote = keep.get("1jATWmDP71v1C8-EjOAA5rFkXyxzeDnWIGz40EDa94IrLGvuVqKW8eleVGMErACbR")
    # print("gnote Title:", gnote.title)
    # print("gnote Text:", gnote.text)
    gameList = gnote.text.splitlines()
    # print("gameList:", gameList)
    return gameList