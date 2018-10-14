import pytest
import unittest
from tweet_parser import TweetParser


class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.tweet_parser = TweetParser()

    def test_get_tweets_returns_list_of_user_tweet_entries(self):
        result = self.tweet_parser.get_tweets('./data/tweet.txt')
        expected_result = [
            ('Alan', 'If you have a procedure with 10 parameters, you probably missed some.'),
            ('Ward', 'There are only two hard things in Computer Science: cache invalidation, naming things and off-by-1 errors.'),
            ('Alan', 'Random numbers should not be generated with a method chosen at random.'),
        ]
        assert result == expected_result