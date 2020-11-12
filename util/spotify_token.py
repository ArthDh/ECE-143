import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import pickle as pkl
import requests


def get_spotify_token(username, scope, redirect_url, client_id, client_secret):
    token = util.prompt_for_user_token(username, scope, client_id,client_secret,redirect_url)

    if token:
        sp = spotipy.Spotify(auth=token)
        print("Token acquired for: ",username)
    else:
        print("Can't get token for", username)