#Tweet.py -hold class here

import time

# Tweet class
class Tweet:
    # Define what happens when a new animal object is created
    #params must be author and text
    def __init__(self, __author, __text):
        #text stores the tweet
        self.__text = __text
        #set author
        self.__author = __author
        #store the time when the tweet was created
        self.__age = time.time()


    #method returns the value of the author field
    def get_author(self):
        return self.__author

    #return the value of the text field
    def get_text(self):
        return self.__text

    #This method calculates the difference between the current time and the value of the __age field.
    #It is to return a string based on the age of the tweet.

    def get_age(self):

        timeDiffCalculation = time.time() - self.__age

    #30s if the tweet was posted 30 seconds ago *must add s m and h so string? yes
        if timeDiffCalculation < 60:
            return str(int(timeDiffCalculation)) + "sec"
        
#15m if the tweet was posted 15 minutes ago
        if timeDiffCalculation/60 < 15:
            return str(int(timeDiffCalculation)) + "min"

#1h if the tweet was posted 1 hour, 10 minutes, and 42 seconds ago (70m 42sec)
        if timeDiffCalculation < 70 and timeDiffCalculation/60 < 42:
            return str(int(timeDiffCalculation)) + "min / sec"
        

