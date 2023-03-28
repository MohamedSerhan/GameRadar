import requests
import constants

def authenticate_twitch():
    url = "https://id.twitch.tv/oauth2/token"
    queryParams = {
        'client_id': constants.TWITCH_CLIENTID,
        'client_secret': constants.TWITCH_CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    req = requests.post(url, params=queryParams)
    return req.json()["access_token"]

def get_release_date_id(game, headers):
    url = "https://api.igdb.com/v4/games"
    body = 'search "' + game + '"; fields name,release_dates;'
    req = requests.post(url, headers=headers, data=body)
    return req.json()[0]["release_dates"][-1]

def get_release_date(game):
    url = "https://api.igdb.com/v4/release_dates"
    twitchToken = authenticate_twitch()
    headers = {
        'Client-ID': constants.TWITCH_CLIENTID,
        'Authorization': "Bearer " + twitchToken
    }
    releaseDateID = get_release_date_id(game, headers)
    body = 'fields *; where id = '+ str(releaseDateID) + ';'
    req = requests.post(url, headers=headers, data=body)
    return req.json()[0]["human"]