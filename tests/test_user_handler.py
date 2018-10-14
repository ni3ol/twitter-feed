import pytest
import unittest
from user_handler import UserHandler


class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.user_handler = UserHandler()

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

    def test_get_new_users_returns_new_users_obtained_from_entry(self):
        user_followers = ('Ward', ['Martin', 'Alan'])
        result = self.user_handler.get_new_users(set(), user_followers)
        expected_result = {'Ward', 'Martin', 'Alan'}
        assert result == expected_result