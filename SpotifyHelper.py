# -*- coding: utf-8 -*-

from OAuth import OAuth
import requests
from json.decoder import JSONDecodeError


class SpotifyHelper:
    def __init__(self):
        oauth = OAuth("*****",
              "*****",
              "http://localhost:3333/callback",
              "https://accounts.spotify.com/authorize/?",
              "https://accounts.spotify.com/api/token",
              scope="user-read-currently-playing")
        token = oauth.get_access_token()
        access_token = token['access_token']
        token_type = token['token_type']
        self.url ="https://api.spotify.com/v1/me/player/currently-playing"
        self.headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": token_type+" "+access_token}


    def get_current_title(self):
        r = requests.get(url=self.url, headers=self.headers)
        try: data = r.json()
        except JSONDecodeError: return False, False, False
        title = data["item"]["name"]
        artist = data["item"]["artists"][0]["name"]
        return data, title, artist
