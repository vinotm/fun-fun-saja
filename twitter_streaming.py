# Import required packages
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import codecs

# Put your access token, access secret, consumer key, and consumer secret here (with quote)
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'
consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# The twitter_data.json below is using dataframe_builder.py script as reference
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        file = codecs.open('twitter_data.json', 'a', 'utf-8')
        file.write(data)
        file.close()
        return True

    def on_error(self, status):
        print status

# BE CAREFUL!! This script will start by wiping out the content of existing twitter_data.json
if __name__ == '__main__':
    file = codecs.open('twitter_data.json', 'w', 'utf-8')
    file.write('')
    file.close()
    l = StdOutListener()
    stream = Stream(auth, l)

# Just edit the track list to stream any keywords you want
    stream.filter(track=['indonesia', 'jakarta'])