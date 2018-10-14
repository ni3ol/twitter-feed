import os
import sys
import warnings

class UserHandler(object):
    def format_user_followers_entry(self, entry):
        '''Takes a user followers entry and formats it into a tuple of user and the users they follow.
        '''
        entry = entry.rstrip()
        entry_without_commas = entry.replace(',', '')
        entry_without_follows = entry_without_commas.replace(' follows', '')
        user_followers_list = entry_without_follows.split(' ')
        user = user_followers_list.pop(0)
        followers_list = user_followers_list
        return user, followers_list

    def get_new_users(self, users, user_followers):
        '''Get new users.
        '''
        new_users = set()
        user = user_followers[0]
        followers = user_followers[1]
        if user not in users:
            new_users.add(user)
        for follower in followers:
            if follower not in users:
                new_users.add(follower)
        return new_users

    def update_user_followers_mapping(self, user_followers_mapping, user_followers):
        '''Return user and updated set of users they follow.
        '''
        user = user_followers[0]
        followers = user_followers[1]
        if user in user_followers_mapping:
            user_followers_mapping[user].update(followers)
            new_followers = user_followers_mapping[user]
        else:
            new_followers = set(followers)
        return user, new_followers