from time import time


class Message:
    def __init__(self, message, timestamp):
        self.__text = message['messages'][0]['text']
        self.__timestamp = timestamp

    def getText(self):
        return self.__text 
    
    
