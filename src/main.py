from logging.handlers import SYSLOG_UDP_PORT
from operator import truediv
from typing import ItemsView
import spotipy
import os
import time
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from slack_sdk import WebClient
from spotipy.oauth2 import SpotifyClientCredentials

#code for setting up the bots with the tokens and also the scopes needed for reading recently played songs along with making a playlist
#also sets up the slack bot client using the slack bot token found in my .env However you cant see my .env because I am not charlie
load_dotenv() 
scope = "user-read-recently-played"
scope2 = "playlist-modify-public";
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
slack_client = WebClient(SLACK_BOT_TOKEN)

#my global spotify variable. Using this to ONLY to get my recently played songs. Scope doesnt allow for anything else.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

most_recent_song = sp.current_user_recently_played(1)


def send_new_song():

    most_recent_song = sp.current_user_recently_played(1)
    most_recent_song_uri = most_recent_song['items'][0]['track']['uri']
    most_recent_song_link = most_recent_song['items'][0]['track']['external_urls']['spotify']

    previous_song = slack_client.conversations_history(channel ='C02R31HJ33Q', limit= 1).data['messages'][0]['text'][1:-1]

    print(previous_song)

    
    if most_recent_song_link != previous_song:       
        slack_client.chat_postMessage(channel='C02R31HJ33Q', text = most_recent_song_link)
     
        message = slack_client.conversations_history(channel ='C02R31HJ33Q', limit= 1)

        data_mes = message.data
        ts = data_mes['messages'][0]['ts']
        slack_client.reactions_add(channel='C02R31HJ33Q', name = 'heart', timestamp=ts)
    


def main():
    while True:
        time.sleep(5)
        send_new_song()


if __name__ == "__main__":
    main()