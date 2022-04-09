from time import time


class Message:
    def __init__(self, message, timestamp):
        self.__text = message
        self.__timestamp = timestamp

    def getText(self):
        return self.__text 
    
    def getTimestamp(self):
        return self.__timestamp
