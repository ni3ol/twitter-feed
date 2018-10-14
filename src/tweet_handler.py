import os
import sys
import warnings

class TweetHandler(object):
    def format_tweet_entry(self, entry):
        '''Takes a tweet and formats it into a tuple containing a user and their followers.
        '''
        user = entry.split(' ', 1)[0]
        user = user.replace('>', '')
        tweet = entry.split(' ', 1)[1]
        tweet = tweet.rstrip()
        if len(tweet) > 140:
            warnings.warn('File contains tweets longer than 140 characters.')
        return user, tweet

    def format_tweet(self, tweet):
        '''Format tweet.
        '''
        return '@{}: {}'.format(tweet[0], tweet[1])