# -*- coding: utf-8 -*-

import requests

class Lyrics():
    def __init__(self, apikey):
        self.apikey = apikey

    def get_lyrics(self, artist, track):
        artist = artist.strip().replace(" ", "%20")
        track = track.strip().replace(" ", "%20")
        url = f"https://orion.apiseeds.com/api/music/lyric/:{artist}/:{track}?apikey={self.apikey}"
        r = requests.get(url)
        data = r.json()
        try:
            return data["result"]["track"]["text"]
        except KeyError:
            return False