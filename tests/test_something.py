import pytest
import unittest
from src.main import get_users_tweets, format_tweet, get_users_from_user_followers_mapping


user_followers_mapping = {
    'Ward': ['Martin', 'Alan'],
    'Alan': ['Martin'],
 }

tweets = [
    ('Alan', 'If you have a procedure with 10 parameters, you probably missed some.'),
    ('Ward', 'There are only two hard things in Computer Science: cache invalidation, naming things and off-by-1 errors.'),
    ('Alan', 'Random numbers should not be generated with a method chosen at random.'),
]


class TestApp(unittest.TestCase):
    def test_get_users_tweets_gets_authors_tweets(self):
        result = get_users_tweets('Alan', user_followers_mapping, tweets)
        expected_result = [tweets[0], tweets[2]]
        assert result == expected_result

    def test_get_users_tweets_gets_authors_and_followers_tweets(self):
        result = get_users_tweets('Ward', user_followers_mapping, tweets)
        expected_result = tweets
        assert result == expected_result

    def test_format_tweet_formats_tweet(self):
        result = format_tweet(tweets[0])
        expected_result = '@Alan: If you have a procedure with 10 parameters, you probably missed some.'
        assert result == expected_result

    def test_get_users_from_user_followers_mapping_gets_user_list(self):
        result = get_users_from_user_followers_mapping(user_followers_mapping)
        expected_result = ['Ward', 'Martin', 'Alan']
        assert sorted(result) == sorted(expected_result)
