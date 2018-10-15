import pytest
import unittest
from user_parser import UserParser


class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.user_parser = UserParser()

    def test_get_users_returns_users_obtained_from_user_file(self):
        result = self.user_parser.get_users('./data/user.txt')
        expected_result = {'Alan', 'Martin', 'Ward'}
        assert result == expected_result

    def test_get_user_followers_mapping_returns_correct_mapping(self):
        """" TODO: Exlain f_users_to_followers_from_user_fileello apping_of_users_to_followers_from_user_file
        """
        result = self.user_parser.get_user_followers_mapping('./data/user.txt')
        expected_result = {'Alan': {'Martin'}, 'Ward': {'Alan', 'Martin'}}
        assert result == expected_result