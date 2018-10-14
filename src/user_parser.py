import os
import sys
import warnings
from user_handler import UserHandler

class UserParser(object):
    def get_users(self, user_file):
        '''Get complete list of all users.
        '''
        users = set()
        user_handler = UserHandler()
        try:
            file = open(user_file, 'r')
        except IOError:
            print('The file cannot be opened.')
        for entry in file:
            try:
                entry = user_handler.format_user_followers_entry(entry)
                new_users = user_handler.get_new_users(users, entry)
            except:
                print('Tweet file entry incorrectly formatted')
            users.update(new_users)
        return users

    def get_user_followers_mapping(self, user_file):
        '''Get mapping of users to the users they follow.
        '''
        user_handler = UserHandler()
        user_followers_mapping = {}
        try:
            file = open(user_file, 'r')
        except IOError:
            print('The file cannot be opened.')
        for entry in file:
            try:
                entry = user_handler.format_user_followers_entry(entry)
                user_followers = user_handler.update_user_followers_mapping(user_followers_mapping, entry)
                user_followers_mapping[user_followers[0]] = user_followers[1]
            except:
                print('Tweet file entry incorrectly formatted')
        return user_followers_mapping