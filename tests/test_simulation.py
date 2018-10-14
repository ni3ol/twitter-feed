import pytest
import unittest
from simulation import Simulation
from user_handler import UserHandler
from tweet_handler import TweetHandler
from user_parser import UserParser
from tweet_parser import TweetParser

class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.user_handler = UserHandler()
        self.tweet_handler = TweetHandler()
        self.user_parser = UserParser()
        self.tweet_parser = TweetParser()
        self.simulation = Simulation()

    def test_format_tweet_formats_tweet(self):
        result = self.tweet_handler.format_tweet(('Alan', 'Hello.'))
        expected_result = '@Alan: Hello.'
        assert result == expected_result

    def test_format_user_followers_entry_returns_user_followers_list(self):
        entry = 'Ward follows Martin, Alan'
        result = self.user_handler.format_user_followers_entry(entry)
        expected_result = ('Ward', ['Martin', 'Alan'])
        assert result == expected_result

    def test_update_empty_user_followers_mapping_returns_user_and_followers_tuple(self):
        user_followers = ('Ward', ['Martin', 'Alan'])
        result = self.user_handler.update_user_followers_mapping({}, user_followers)
        expected_result = ('Ward', {'Martin', 'Alan'})
        assert result == expected_result

    def test_update_user_followers_mapping_returns_user_and_updated_followers_tuple(self):
        user_followers = ('Ward', ['Martin', 'Alan'])
        result = self.user_handler.update_user_followers_mapping({'Ward': {'Martin'}}, user_followers)
        expected_result = ('Ward', {'Martin', 'Alan'})
        assert result == expected_result

    def test_format_tweet_entry_returns_user_and_tweet_tuple(self):
        entry = 'Alan> Hello.\n'
        result = self.tweet_handler.format_tweet_entry(entry)
        expected_result = ('Alan', 'Hello.')
        assert result == expected_result

    def test_get_new_users_returns_new_users_obtained_from_entry(self):
        user_followers = ('Ward', ['Martin', 'Alan'])
        result = self.user_handler.get_new_users(set(), user_followers)
        expected_result = {'Ward', 'Martin', 'Alan'}
        assert result == expected_result

    def test_get_users_returns_users_obtained_from_user_file(self):
        result = self.user_parser.get_users('./data/user.txt')
        expected_result = {'Alan', 'Martin', 'Ward'}
        assert result == expected_result

    def test_get_user_followers_mapping_returns_mapping_of_users_to_followers_from_user_file(self):
        result = self.user_parser.get_user_followers_mapping('./data/user.txt')
        expected_result = {'Alan': {'Martin'}, 'Ward': {'Alan', 'Martin'}}
        assert result == expected_result

    def test_get_tweets_returns_list_of_user_tweet_entries(self):
        result = self.tweet_parser.get_tweets('./data/tweet.txt')
        expected_result = [
            ('Alan', 'If you have a procedure with 10 parameters, you probably missed some.'),
            ('Ward', 'There are only two hard things in Computer Science: cache invalidation, naming things and off-by-1 errors.'),
            ('Alan', 'Random numbers should not be generated with a method chosen at random.'),
        ]
        assert result == expected_result

    def test_simulation_returns_simulation_of_users_and_tweets_as_list(self):
        users = {'Ward', 'Martin', 'Alan'}
        user_followers_mapping = {'Ward': {'Martin', 'Alan'}}
        tweets = [('Ward', 'Random numbers should not be generated with a method chosen at random.')]
        result = self.simulation.get_simulation(users, user_followers_mapping, tweets)
        expected_result = ['Alan', 'Martin', 'Ward', '@Ward: Random numbers should not be generated with a method chosen at random.'] 
        assert result == expected_result

