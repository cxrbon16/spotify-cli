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
        return self.client.current_user_playing_track()['item']['name']

    def next_track(self, args):
        return self.client.next_track()
    
    def get_playlists(self, args):
        plists = self.client.current_user_playlists()
        for i in range(len(plists['items'])):
            print(plists['items'][i]['name'])
    
    def adjust_volume_directly(self, args):
        self.client.volume(int(args.adj))
        time.sleep(0.2)
    def get_current(self, args):
        print(f"""
          current display name: {self.get_display_name()}
          current track name: {self.get_current_track_name()},
          current volume level: {self.get_current_volume()},
           """)
    
