import os
import sys
import warnings
from tweet_handler import TweetHandler

class TweetParser(object):
    def get_tweets(self, tweet_file):
        '''Get user and tweet and output as tuple.
        '''
        tweets = []
        tweet_handler = TweetHandler()
        try:
            file = open(tweet_file, 'r')
        except IOError:
            print('The file cannot be opened.')
        for entry in file:
            try:
                formatted_entry = tweet_handler.format_tweet_entry(entry)
            except:
                print('Tweet file entry incorrectly formatted')
            tweets.append(formatted_entry)
        return tweets