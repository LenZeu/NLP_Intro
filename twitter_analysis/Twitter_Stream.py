## import packages
from pymongo import MongoClient
import json
import tweepy
import datetime


MONGO_HOST= 'mongodb://localhost/twitterdb_final'
WORDS = ['Trump','Xi Jinping', 'Maduro','Kim Jong Un','Elizabeth Warren', 'Theresa May']
CONSUMER_KEY = "gpgdPxounB8FS7eP3OnID8aXL"
CONSUMER_SECRET = "6V2OTyVDqzUswhD84ocdC9JBTAfo2QNwEt84TJdACiVni6G1Ei"
ACCESS_TOKEN = "1121843430064361477-UMOytT7TR6nrh3gqzhMDJIHk2wqMUc"
ACCESS_TOKEN_SECRET = "labFTJ2xumZgeT77zmuSLuMASosGx9dap4Q2h2OvRXmkU"


class StreamListener(tweepy.StreamListener):
    # This is a class provided by tweepy to access the Twitter Streaming API.

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        # This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            client = MongoClient(MONGO_HOST)

            # Use twitterdb_final database.
            db = client.twitterdb_final

            # Decode the JSON from Twitter
            t = json.loads(data)

            # Pull important data from the tweet to store in the database.
            tweet_id = t['id_str']  # The Tweet ID from Twitter in string format
            username = t['user']['screen_name']  # The username of the Tweet author
            followers = t['user']['followers_count']  # The number of followers the Tweet author has
            tweet_text = t['text']  # The entire body of the Tweet
            hashtags = t['entities']['hashtags']  # Any hashtags used in the Tweet
            date = t['created_at']  # The timestamp of when the Tweet was created
            lang = t['lang']  # The language of the Tweet

            # Convert the timestamp string given by Twitter to a date object called "created". This is more easily manipulated in MongoDB.
            created = datetime.datetime.strptime(date, '%a %b %d %H:%M:%S +0000 %Y')

            # Load all of the data into the variable "tweet" that will be stored into the database
            tweet = {'id': tweet_id, 'username': username, 'followers': followers, 'text': tweet_text,
                     'hashtags': hashtags, 'language': lang, 'created': created}

            # print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created))

            # Optional - Print the username and text of each Tweet to your console in realtime as they are pulled from the stream
            print(username + ':' + ' ' + tweet_text)

            # insert the data into the mongoDB into a collection called twitter_stream
            # if twitter_stream doesn't exist, it will be created.
            db.twitter_stream_sample.insert_one(tweet)

        except Exception as e:
            print(e)

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        # Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
        listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
        streamer = tweepy.Stream(auth=auth, listener=listener)
        print("Tracking: " + str(WORDS))
        streamer.filter(track=WORDS)
