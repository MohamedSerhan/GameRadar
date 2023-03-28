import gkeepapi
import constants
from . import IGDBIntegration as igdb

keep = gkeepapi.Keep()
keep.login(constants.GKEEP_USERNAME,constants.GKEEP_PASSWORD)

def get_video_game_list_from_keep():
    glist = keep.get(constants.GKEEP_NOTEID)
    game_list = glist.text.splitlines()
    return game_list

def format_game_entry(game):
    # Check game entry release date amd store it
    release_date = igdb.get_release_date(game)
    print("releaseDate:", release_date)
    return game + " - " + release_date

def format_game_from_list(game):
    second_index = game.index('-') - 2
    return game[3:second_index].strip()

def check_list_for_entry_and_append(entry, game_list, GUI_pop_up):
    append_game = True
    for game_value in game_list:
        game = format_game_from_list(game_value)
        if entry in game:
            # Notify user entry already exists if game is within array
            append_game = False
            GUI_pop_up()
    new_game_list = game_list
    if append_game == True:
        print('Adding',entry,'to game list')
        new_game_list.append(format_game_entry(entry))
    return new_game_list

def write_game_list_to_keep(game_list):
    glist = keep.get(constants.GKEEP_NOTEID)
    idx = list(range(len(glist.items)))
    for game in idx:
        item = glist.items[0]
        item.delete()
    for game in game_list:
        glist.add(game.replace('☐','').strip(), False, gkeepapi.node.NewListItemPlacementValue.Bottom)
    keep.sync()
