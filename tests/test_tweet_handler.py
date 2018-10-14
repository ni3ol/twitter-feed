import pytest
import unittest
from tweet_handler import TweetHandler


class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.tweet_handler = TweetHandler()

    def test_format_tweet_formats_tweet(self):
        result = self.tweet_handler.format_tweet(('Alan', 'Hello.'))
        expected_result = '@Alan: Hello.'
        assert result == expected_result

    def test_format_tweet_entry_returns_user_and_tweet_tuple(self):
        entry = 'Alan> Hello.\n'
        result = self.tweet_handler.format_tweet_entry(entry)
        expected_result = ('Alan', 'Hello.')
        assert result == expected_result