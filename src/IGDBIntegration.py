import requests
import constants

def authenticateTwitch():
    url = "https://id.twitch.tv/oauth2/token"
    queryParams = {
        'client_id': constants.TWITCH_CLIENTID,
        'client_secret': constants.TWITCH_CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    req = requests.post(url, params=queryParams)
    return req.json()["access_token"]

def getReleaseDateID(game, headers):
    url = "https://api.igdb.com/v4/games"
    body = 'search "' + game + '"; fields name,release_dates;'
    req = requests.post(url, headers=headers, data=body)
    return req.json()[0]["release_dates"][-1]

def getReleaseDate(game):
    url = "https://api.igdb.com/v4/release_dates"
    twitchToken = authenticateTwitch()
    headers = {
        'Client-ID': constants.TWITCH_CLIENTID,
        'Authorization': "Bearer " + twitchToken
    }
    releaseDateID = getReleaseDateID(game, headers)
    body = 'fields *; where id = '+ str(releaseDateID) + ';'
    req = requests.post(url, headers=headers, data=body)
    return req.json()[0]["human"]