class Message:
    def __init__(self, message):
        self.__text = message['messages'][0]['text']

    def getText(self):
        return self.__text 
