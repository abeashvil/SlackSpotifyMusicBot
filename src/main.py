from operator import truediv
from typing import ItemsView
import spotipy
import os
import time
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from slack_sdk import WebClient
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv() 
scope = "user-read-recently-played"
scope2 = "playlist-modify-public";
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
slack_client = WebClient(SLACK_BOT_TOKEN)

# recent_msg = slack_client.conversations_history(channel ='C02R31HJ33Q', limit= 1)
# data_mes = recent_msg.data['messages'][0]['text']
# while data_mes != 'stop' and data_mes != 'Stop':
#     time.sleep(10)
#     recent_msg = slack_client.conversations_history(channel ='C02R31HJ33Q', limit= 1)
#     data_mes = recent_msg.data['messages'][0]['text']
#     print(data_mes)


most_recent_song = sp.current_user_recently_played(1)


most_recent_song_uri = most_recent_post['items'][0]['track']['uri']
most_recent_song_link = most_recent_post['items'][0]['track']['external_urls']['spotify']

previous_song_link

while True:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    #most recent song listened to
    most_recent_song = sp.current_user_recently_played(1)


    most_recent_song_uri = most_recent_post['items'][0]['track']['uri']
    most_recent_song_link = most_recent_post['items'][0]['track']['external_urls']['spotify']


    slack_client.chat_postMessage(channel='C02R31HJ33Q', text = most_recent_song_link)


    message = slack_client.conversations_history(channel ='C02R31HJ33Q', limit= 1)


    data_mes = message.data
    ts = data_mes['messages'][0]['ts']
    slack_client.reactions_add(channel='C02R31HJ33Q', name = 'heart', timestamp=ts)
    # slack_client.reactions_add()

