# Spotify API

## How to use

1. Install the [Spotipy](https://spotipy.readthedocs.io) library using `pip install spotipy`
1. Follow these instructions to register an application and get a client ID and client secret: https://developer.spotify.com/documentation/web-api/quick-start
1. Set up the library like so, using your client ID and client secret from the previous step:
   ```python
   import spotipy
   from spotipy.oauth2 import SpotifyClientCredentials

   credentials = SpotifyClientCredentials(client_id='xx', client_secret='yy')
   spotify = spotipy.Spotify(client_credentials_manager=credentials)
   ```
1. Now the possibilities are endless! Check out Spotipy's [API reference](https://spotipy.readthedocs.io/en/2.16.1/#api-reference) to view all the available methods, and go through their examples [here](https://github.com/plamere/spotipy/tree/master/examples). Spotify's official [documentation](https://developer.spotify.com/documentation/web-api/reference) will also help you find out what's possible with their API.

## Example project

[spotify_mood_bot.py](spotify_mood_bot.py): A chatbot that asks you how you're feeling, recommends a few genres of music, then plays a song from the genre you choose.
