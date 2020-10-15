# -*- coding: utf-8 -*-

import requests

class MusixmatchHelper():
    def __init__(self, apikey):
        self.apikey = apikey

    def search(self, track, artist):
        url = "http://api.musixmatch.com/ws/1.1/track.search&apikey="+self.apikey
        if track:
            track = track.strip().replace(" ", "%20")
            url = url+"&q_track="+track
        if artist:
            artist = artist.strip().replace(" ", "%20")
            url = url+"&q_artist="+artist
        url = url+"&page_size=1"
        url = url+"&s_artist_rating=asc"
        r = requests.get(url=url)
        data = r.json()
        return data["message"]["body"]["track_list"][0]["track"]

    def get_lyrics(self, data):
        track_id = data["track_id"]
        url = "https://api.musixmatch.com/ws/1.1/track.lyrics.get&apikey="+self.apikey
        url = url+"&track_id="+str(track_id)
        r = requests.get(url=url)
        data = r.json()
        return data






mx = MusixmatchHelper("*************")
data = mx.get_lyrics(mx.search("Got You On My Mind", "NF"))
data = data["message"]["body"]["lyrics"]["lyrics_body"]
f = open("text.txt", 'w')
f.write(data)
f.close()
