# from asyncio.windows_events import NULL
import os
from dotenv import load_dotenv
from slack_sdk import WebClient

from Message import Message

load_dotenv()
SLACK_BOT_TOKEN =  os.environ['SLACK_BOT_TOKEN']
bot = WebClient(SLACK_BOT_TOKEN)

def main():
    # creating a slack channel for the bot to use. This will be the main channel that it will talk in/ people can post images in
    channel = NULL
    try:
        channel = bot.conversations_create(name = "imageoftheweek", is_private= False)
    except:
        print("failed, channel already exists")
        # creates a list of all the channels in the slack conversation
        channelList = bot.conversations_list()['channels']

        #if the channel already exists, we need to set the channel variable to it and also have the bot join the channel
        for i in range(len(channelList)):
            if(channelList[i]["name"] == "imageoftheweek"):
                channel = channelList[i]
                bot.conversations_join(channel = channel['id'])

    channelId = channel['id']

    #grabbing the actual message String from the last message
    message = Message(bot.conversations_history(channel = channelId, limit = 1))


if __name__ == "__name__":
    main()