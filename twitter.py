#This program manages Tweets
import Tweet
import pickle

#Global constants for menu choices
MAKE_TWEET = 1
VIEW_TWEET = 2
SEARCH_TWEET = 3
QUIT = 4

#Global constant for the filename
FILENAME = 'tweets.dat'

#main function
def main():
    #load the existing tweet list
    #and assign it to mytweets
    mytweets = load_tweets()

    #initialize the variable for the user's choice
    choice = 0

    #process menu selections until the user
    #wants to quit the program
    while choice != QUIT:
        #Get the user's menu choice
        choice = get_menu_choice()

        #Process the choice
        if choice == MAKE_TWEET:
            make_tweet(mytweets)
        elif choice == VIEW_TWEET:
            view_recent_tweet(mytweets)
        elif choice == SEARCH_TWEET:
            search_tweet(mytweets)
        elif choice == QUIT:
            print('Thank you for using the Tweet Manager!')
            
#the load_tweets function opens the
#tweets.dat file and unpickels it for use
def load_tweets():
    try:
        #Open the tweets.dat file
        in_file = open(FILENAME, 'rb')

        #unpickle the list
        tweet_list = pickle.load(in_file)

        #close the tweets.data file
        in_file.close()
    except IOError:
        #Could not open file so create
        #an empty list
        tweet_list = []

    #return the list
    return tweet_list

#The get_menu_choice function displays the menu
#and gets a validated choice form the user
def get_menu_choice():
    #print menu
    print()
    print('Tweet Menu')
    print('----------')
    print('1. Make a Tweet')
    print('2. View Recent Tweets')
    print('3. Search Tweets')
    print('4. Quit')
    print()

    #Get the user's choice and validate
    while True:
        try:
            choice = int(input('What would you like to do? '))
            if choice < MAKE_TWEET or choice > QUIT:
                print('Please select a valid option.')
                print()
                continue            
        except ValueError:
            print('Please enter a numeric value.')
            print()
        else:
            break
            
            
    #Return user's choice
    return choice

#The make_tweet function saves a new tweet into the
#tweet.dat file
def make_tweet(mytweets):
    #Get user name 
    author = input('What is your name? ')

    #Get tweet
    text = input('What would you like to tweet? ')

    #Check length of user_tweet is under 140 characters
    while len(text) > 140:
        print('Tweets can only be 140 characters')
        print()
        text = input('What would you like to tweet? ')1    

    #only save file if text is less than 140 characters
    #to prevent records with empty tweets
    if len(text) <= 140:
        #Create a tweet object named tweet-entry
        tweet_entry = Tweet.Tweet(author, text)

        #Add tweet_entry to beginning of mytweets list    
        mytweets.insert(0, tweet_entry)

        #Save the mytweets list to a file
        save_tweets(mytweets)
    
        print(author, ', your tweet has been saved.', sep='')    

#The view_recent_tweet function prints the last 5 tweets
def view_recent_tweet(mytweets):   
    print()
    print('Recent Tweets')
    print('-------------')    

    #Check if list is empty and act
    #accordingly
    if len(mytweets) == 0:
        print('There are no recent tweets.')
    else:
        #Get the first 5 elements of list
        recent_tweets = mytweets[:5]
        #Iterate through loop and print object attributes
        for obj in recent_tweets:
            print(obj.get_author(), '-', obj.get_age())
            print(obj.get_text())
            print()

#The search_tweet uses a search term to search
#for a tweets containing the term
def search_tweet(mytweets):
    #Create search_count variable to determine if
    #the serach_term was found in the list
    search_count = 0

    #check if list is empty and act accordingly
    if len(mytweets) == 0:
        print('There are no tweets to search.')
    else:
        #Get term to search for
        search_term = input('What would you like to search for? ')
        print()
        print('Search Results')
        print('--------------') 

        #Iterate through loop and if search term is found
        #print the tweets
        for obj in mytweets:
            if search_term in obj.get_text():
                search_count += 1
                print(obj.get_author(), '-', obj.get_age())
                print(obj.get_text())
                print()

        #If the search_term was not found in the list print 
        if search_count == 0:
            print('No tweets contained', search_term)    

       
#The save_tweets function writes/saves file to disk    
def save_tweets(mytweets):
    #Open file for writing
    out_file = open(FILENAME, 'wb')

    #Pickle the list and save it
    pickle.dump(mytweets, out_file)

    #Close the file
    out_file.close()    

#Call main function
main()


        

    
    



























    
    
