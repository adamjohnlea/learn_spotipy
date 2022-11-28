import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from configparser import ConfigParser

# retrieve the stored credentials
config = ConfigParser()
config.read('credentials.cfg')
client_id = config['spotify_api']['client_id']
client_secret = config['spotify_api']['client_secret']

# authenticate with Spotipy
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

# spotify object is created
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()

