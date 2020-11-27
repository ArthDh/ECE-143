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
    return sp
        
        
class Artist:
    '''
    Class for ease of handling of JSON objects 
    '''
    def __init__(self, _id,name, genres, track_id, track_name, pop):
        self._id = _id
        self.name = name
        self._genres = genres
        self._track_id = track_id
        self._track_name = track_name
        self._pop = pop
        

class ArtistCollection:
    '''
    Collection of Artist class objects
    '''
    def __init__(self, artists = None):
        self.artists = artists
    
    @property
    def seed_artists(self):
        return [ a._id for a in self.artists]
    
    @property
    def seed_genres(self):
        temp_genres = []
        for a in self.artists:
            temp_genres.extend(a._genres)
        return temp_genres
    
    @property
    def seed_tracks(self):
        temp_tracks = []
        for a in self.artists:
            temp_tracks.append(a._track_id)
        return temp_tracks

def get_artist(artists, sp):
    '''
    Returns list of Artist class objects for ease of use
    '''
    artist = []
    for a in artists:
        res = sp.search(q=a, type='artist')['artists']['items'][0]
        track = sp.search(q=a, type='track')['tracks']['items'][0]
        temp = Artist(res['id'], res['name'], res['genres'], track['id'], track['name'], track['popularity'])
        artist.append(temp)
    return artist

def get_features(artist, sp, features):
    d = dict()
    audio_features = sp.audio_features(artist._track_id)[0]
    for feats in features:
        if feats not in d.keys():
            if feats in audio_features:
                d[feats] = audio_features[feats]
    d['popularity'] = artist._pop
    return d


def get_recommendations(artists, sp, lim = 1):
  
    list_of_artists = artists
    pred_artist_col = ArtistCollection(get_artist(list_of_artists, sp))
    
    recommendations = []
    recommendations.append(sp.recommendations(\
                       seed_artists=pred_artist_col.seed_artists, \
                       seed_genres=pred_artist_col.seed_genres[:1], \
                       seed_tracks=pred_artist_col.seed_tracks, limit=lim))
    
    return recommendations