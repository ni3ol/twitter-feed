import os
import sys
import warnings
from tweet_handler import TweetHandler, FormatError


class TweetParser(object):
    def get_tweets(self, tweet_filename):
        '''Get user and tweet and output as tuple.
        '''
        tweets = []
        tweet_handler = TweetHandler()
        try:
            with open(tweet_filename, 'r') as tweet_file:
                for entry in tweet_file:
                    formatted_entry = tweet_handler.format_tweet_entry(entry)
                    tweets.append(formatted_entry)
                return tweets
        except IOError:
            print('The file cannot be opened.')
        except FormatError:
            print('Tweet file entry incorrectly formatted')
        