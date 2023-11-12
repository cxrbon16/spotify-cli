import os
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class processor:
    def __init__(self, spotipy_auth: spotipy.client.Spotify):
        self.client = spotipy_auth
    
    def get_display_name(self):
        return self.client.current_user()['display_name']

    def get_current_volume(self):
        return self.client.current_playback()['device']['volume_percent']
    
    def get_current_track_name(self):
        self.client.current_user_playing_track()['item']['name']

    def next_track(self):
        return self.client.next_track()

    def adjust_volume(self, adj: str):
        current_vol = self.get_current_volume()
        change = 0
        for i in adj:
            if i == "+":
                change += 10
            elif i == "-":
                change -= 10
            else:
                return "invalid input brah."
        if current_vol + change > 100:
            self.client.volume(100)
        elif current_vol + change <= 0:
            self.client.volume(0)
        else:
            self.client.volume(current_vol + change)
        
        time.sleep(0.2)
        return self.get_current_volume()
        
    def adjust_volume_directly(self, adj: int):
        self.client.volume(int(adj))
        time.sleep(0.2)
        return self.get_current_volume()
    
