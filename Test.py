# -*- coding: utf-8 -*-

import time
from SpotifyHelper import SpotifyHelper
from Lyrics import Lyrics

sp = SpotifyHelper()
l = Lyrics("******")


while True:
    data, title, artist = sp.get_current_title()
    if data:
        lyrics = l.get_lyrics(artist, title)
        print(title)
        print(artist)
        if lyrics: print(lyrics)
        else: print("Keine Lyrics")
    else:
        print("Spotify nicht offen, oder kein Titel wird abgespielt.")


    while True:
        data, new_title, temp = sp.get_current_title()
        if data:
            if not title == new_title:
                break
            remaining = (int(data["item"]["duration_ms"]) - int(data["progress_ms"]))/1000
            if remaining/4 >= 20: t = 10
            else: t = remaining/4
            if t <= 0.1:
                break
            time.sleep(t)
        else:
            time.sleep(10)
