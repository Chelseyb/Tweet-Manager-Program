#twitter.py (main code to run)

from Tweet import Tweet
import pickle
import os.path

def main():

    tweets = [] 
    
#run these two while the user does not say no., TYPE then NAME

    while True:
        print('Tweet Menu')
        print('----------------\n')
        print(" 1. Make a tweet \n 2. View recent tweets \n 3. Search Tweets \n 4. Quit")

        pick1Or2 = int(input('What would you like to do?: '))
        

                


        #have to check to see how long the tweet is
        if(pick1Or2 == 1):
            author = input("What is your name? ")
            text =str(input("What would you like to tweet: "))
            if len(text) < 140:
                tweeting = Tweet(author,text)
                tweets.append(tweeting)
                print("Tweets\n")
                for tweet in tweets:
                    print(tweet.get_author() + "," + " your tweet ["+tweet.get_text() +"], has been saved")
                tweeting = text
                file=open("tweets.dat","wb")
                pickle.dump(tweeting,file)
                file.close()
            
        
            else:
                print("Tweets  much be less than 140 chars\n")
                continue
            #print the last five tweets WITH date
        
        if(pick1Or2 == 2):
            try:
                if len(tweets) == 0:
                    print("No recent tweets but past tweets are in the file")
                else:
                    for tweetList in range(len(tweets)-1, len(tweets)-4,-1):
                        print("Author: " + tweets[tweetList].get_author())
                        print("Tweet:" + tweets[tweetList].get_text())
                        print("Date: " +tweets[tweetList].get_age()+"\n")
            except:
                print("end of list")


        if(pick1Or2 == 3):
            searching = False
            if len(tweets) == 0:
                print("No tweets yet")
            findThis = str(input("Enter what you are looking for: "))
            index = 0
            for index in range(len(tweets)-1,0,-1):
                if findThis in tweets[index].get_text():

                    print("Author: " + tweets[index].get_author())
                    print("Tweet:" + tweets[index].get_text())
                    print("Date: " +tweets[index].get_age()+"\n")
                else:
                    print("Those chars are not in the tweets")


            
        if(pick1Or2 ==4):
            print("That's all folks!")
            break

        
         


      #  print('\nTweets:\n')
       #format: name, tweet has been saved (not the tweet)
      #  for tweet in tweets:
           # print(tweet.get_author() + "," + " your tweet ["+tweet.get_text() +"], has been saved")
           
#before i ask again the tweets have to be saved in a file called tweets.dat
       
        
         

        choice = input('\nWould you like to go again? (y/n)? ')
        if choice.lower() == 'n':
            tweeting = text
            file=open("tweets.dat","wb")
            pickle.dump(tweeting,file)
            file.close()
            print("All tweets saved to tweets.dat, goodbye")
            break
        else:
            print("going again!")
           

main()
