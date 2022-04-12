# SlackSpotifyMusicBot

#This bot sends a song from my recently listened to songs on spotify to the specified slack channel every hour over the course of a day, and then resends the winning song which has the most reactions by the end of the day.

This bot was fully written in python, but will be rewritten in Javascript, or atleast for the Spotify API part of the project. 
To Note: This project is very much still a work in progress, and I would like to have the bot working for all spotify accounts, and not just mine. 
  *Current Issues:
      - Spotipy API authentication does not support single login authentication, rahter requires the use of a           token. To fix this, the spotify section of the code must be written in the Javascript equivalent               library, which does support single login authentification.
      -Inefficient code, which can be fixed by having program run only at specified times, storing the results        in a database, and then checking the results after the day ends.

How my code works: 
  I have a few important method chunks which control most of whats going on. First I created a Message class 
  which stores the timestamp and text of a message. This is needed because the most efficient way of  retrieving 
  past slack messages is with the use of the timestamp from that message. I also needed the text of the message 
  for a later issue I will address. Next, I created a setup method which essentially creates a slack channel 
  for the bot to use, since I want the bot to only operate in that channel and not spam other channels. The 
  function also checks if the channel already exists, and if so, it does not create a new channel, rather it 
  joins the pre-existing one. Next I created the send_new_song function, which fetches my most recently 
  listened to song, checks if its equal to the previously sent song, and sends it in the channel if they are   different. After this, I iterate through all the songs and check the amount of reactions under the song to   see which one is the best, and then I send that song at the end of the time period. 

What I learned during this project...

This project was my first experience with any form of an API, so learning both was a bit confusing. I spent a lot of my time originally researching how to set up a bot for both slack and spotify. The setup  of the bots was the most difficult part for me. Next I spent time planning out how I would set up the bot to periodically send songs. I needed to fetch my most recent song, go through the data and find what I needed, find out which channel I would send that data too, and then send it. Overall, I think I learned a great deal about API's and how to use bots, and I feel fairly confident in tackling such things from now on. 

I plan of implementing this bot soon on slack, but I would prefer that it works for all users spotify accounts rather than just mine before doing so. 
