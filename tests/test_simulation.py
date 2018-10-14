import pytest
import unittest
from simulation import Simulation


class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation()

    def test_simulation_returns_simulation_of_users_and_tweets_as_list(self):
        users = {'Ward', 'Martin', 'Alan'}
        user_followers_mapping = {'Ward': {'Martin', 'Alan'}}
        tweets = [('Ward', 'Random numbers should not be generated with a method chosen at random.')]
        result = self.simulation.get_simulation(users, user_followers_mapping, tweets)
        expected_result = ['Alan', 'Martin', 'Ward', '@Ward: Random numbers should not be generated with a method chosen at random.'] 
        assert result == expected_result

