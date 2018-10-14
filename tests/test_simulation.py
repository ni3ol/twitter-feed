import pytest
import unittest 
from src.main import format_user_followers_entry, get_new_users, update_user_followers_mapping, get_users, get_user_followers_mapping, format_tweet_entry, format_tweet, get_tweets, get_simulation

class TestSimulation(unittest.TestCase):
    def test_format_tweet_formats_tweet(self):
        result = format_tweet(('Alan', 'Hello.'))
        expected_result = '@Alan: Hello.'
        assert result == expected_result

    def test_format_user_followers_entry_returns_user_followers_list(self):
        entry = 'Ward follows Martin, Alan'
        result = format_user_followers_entry(entry)
        expected_result = ('Ward', ['Martin', 'Alan'])
        assert result == expected_result

    def test_update_empty_user_followers_mapping_returns_user_and_followers_tuple(self):
        user_followers = ('Ward', ['Martin', 'Alan'])
        result = update_user_followers_mapping({}, user_followers)
        expected_result = ('Ward', {'Martin', 'Alan'})
        assert result == expected_result

    def test_update_user_followers_mapping_returns_user_and_updated_followers_tuple(self):
        user_followers = ('Ward', ['Martin', 'Alan'])
        result = update_user_followers_mapping({'Ward': {'Martin'}}, user_followers)
        expected_result = ('Ward', {'Martin', 'Alan'})
        assert result == expected_result

    def test_format_tweet_entry_returns_user_and_tweet_tuple(self):
        entry = 'Alan> Hello.\n'
        result = format_tweet_entry(entry)
        expected_result = ('Alan', 'Hello.')
        assert result == expected_result

    def test_get_new_users_returns_new_users_obtained_from_entry(self):
        user_followers = ('Ward', ['Martin', 'Alan'])
        result = get_new_users(set(), user_followers)
        expected_result = {'Ward', 'Martin', 'Alan'}
        assert result == expected_result

    def test_get_users_returns_users_obtained_from_user_file(self):
        result = get_users('./data/user.txt')
        expected_result = {'Alan', 'Martin', 'Ward'}
        assert result == expected_result

    def test_get_user_followers_mapping_returns_mapping_of_users_to_followers_from_user_file(self):
        result = get_user_followers_mapping('./data/user.txt')
        expected_result = {'Alan': {'Martin'}, 'Ward': {'Alan', 'Martin'}}
        assert result == expected_result

    def test_get_tweets_returns_list_of_user_tweet_entries(self):
        result = get_tweets('./data/tweet.txt')
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
        result = get_simulation(users, user_followers_mapping, tweets)
        expected_result = ['Alan', 'Martin', 'Ward', '@Ward: Random numbers should not be generated with a method chosen at random.'] 
        assert result == expected_result

