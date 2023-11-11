import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('CLIENT_ID')

scope = "user-library-read user-modify-playback-state user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_playing_track()
print(results['item']['artists'][0]['name'], "--", results['item']['name'])
sp.next_track()
print(results['item']['artists'][0]['name'], "--", results['item']['name'])
