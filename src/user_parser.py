import os
import sys
import warnings
from user_handler import UserHandler, FormatError


class UserParser(object):
    def get_users(self, user_filename):
        '''Get complete list of all users.
        '''
        users = set()
        user_handler = UserHandler()
        try:
            with open(user_filename, 'r') as user_file:
                for entry in user_file:
                    entry = user_handler.format_user_followers_entry(entry)
                    new_users = user_handler.get_new_users(users, entry)
                    users.update(new_users)
                return users

        except IOError:
            print('The file cannot be opened.')
        except FormatError:
            print('Tweet file entry incorrectly formatted')
       

    def get_user_followers_mapping(self, user_filename):
        '''Get mapping of users to the users they follow.
        '''
        user_handler = UserHandler()
        user_followers_mapping = {}
        try:
            with open(user_filename, 'r') as user_file:
                for entry in user_file:
                    entry = user_handler.format_user_followers_entry(entry)
                    user_followers = user_handler.update_user_followers_mapping(user_followers_mapping, entry)
                    user_followers_mapping[user_followers[0]] = user_followers[1]
                return user_followers_mapping
        except IOError:
            print('The file cannot be opened.')
        except FormatError:
            print('Tweet file entry incorrectly formatted')
       