# Import required packages
import json
import pandas as pd

# This is the path of JSON file to store the mined data. Just edit to suit to your local repository
path = 'C:/Users/asus/PycharmProjects/Twitter Mining/twitter_data.json'

tweets_data = []
tweets_file = open(path, 'r')
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

tweets = pd.DataFrame()

# Fields from raw JSON data that will be copied to output table
tweets['screen_name'] = map(lambda x: x['user']['screen_name'], tweets_data)
tweets['created_at'] = map(lambda x: x['timestamp_ms'], tweets_data)
tweets['language'] = map(lambda x: x['lang'], tweets_data)
tweets['text'] = map(lambda x: x['text'], tweets_data)
tweets['quote_count'] = map(lambda x: x['quote_count'], tweets_data)
tweets['reply_count'] = map(lambda x: x['reply_count'], tweets_data)
tweets['retweet_count'] = map(lambda x: x['retweet_count'], tweets_data)
tweets['favorite_count'] = map(lambda x: x['favorite_count'], tweets_data)

# Edit the output table path to suit your local repository
tweets.to_csv(path_or_buf="C:/Users/asus/PycharmProjects/Twitter Mining/data.csv", index=False, encoding='utf-8')
