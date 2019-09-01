import time

class Tweet:

    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        self.__age = time.time() #current time in seconds

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_age(self):
        #Difference between when get_age getter was called and
        #__age was initialized, in seconds
        seconds = int(time.time() - self.__age)

        #Difference between when get_age getter was called and
        #__age was initialized, in minutes
        minutes = int(seconds / 60)

        #Difference between when get_age getter was called and
        #__age was initialized, in hours
        hours = int(minutes / 60)

        if seconds >= 0 and seconds < 60:
            return str(seconds) + 's'
        elif seconds >= 60 and seconds < 3600:
            return str(minutes) + 'm'
        else:
            return str(hours) + 'h'

   
       
        
        

    
        

    
