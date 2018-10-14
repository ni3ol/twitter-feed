import sys

def format_user_followers_entry(entry):
    '''Takes a user followers entry and formats it into a tuple of user and the users they follow.
    '''
    entry = entry.rstrip()
    entry_without_commas = entry.replace(',', '')
    entry_without_follows = entry_without_commas.replace(' follows', '')
    user_followers_list = entry_without_follows.split(' ')
    user = user_followers_list.pop(0)
    followers_list = user_followers_list
    return user, followers_list

def get_new_users(users, user_followers):
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

def update_user_followers_mapping(user_followers_mapping, user_followers):
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

def get_users(user_file):
    '''Get complete list of all users.
    '''
    users = set()
    file = open(user_file, 'r')
    for entry in file:
        entry = format_user_followers_entry(entry)
        new_users = get_new_users(users, entry)
        users.update(new_users)
    return users

def get_user_followers_mapping(user_file):
    '''Get mapping of users to the users they follow.
    '''
    user_followers_mapping = {}
    file = open(user_file, 'r')
    for entry in file:
        entry = format_user_followers_entry(entry)
        user_followers = update_user_followers_mapping(user_followers_mapping, entry)
        user_followers_mapping[user_followers[0]] = user_followers[1]
    return user_followers_mapping

def format_tweet_entry(entry):
    '''Takes a tweet and formats it into a tuple containing a user and their followers.
    '''
    user = entry.split(' ', 1)[0]
    user = user.replace('>', '')
    tweet = entry.split(' ', 1)[1]
    tweet = tweet.rstrip()
    return user, tweet

def format_tweet(tweet):
    '''Format tweet.
    '''
    return '@{}: {}'.format(tweet[0], tweet[1])

def get_tweets(tweet_file):
    '''Get user and tweet and output as tuple.
    '''
    tweets = []
    file = open(tweet_file, 'r')
    for entry in file:
        formatted_entry = format_tweet_entry(entry)
        tweets.append(formatted_entry)
    return tweets

def get_simulation(users, user_followers_mapping, tweets):
    '''Return ordered users and their tweets.
    '''
    simulation = []
    for user in sorted(users):
        simulation.append(user)
        try:
            followers = user_followers_mapping[user]
        except:
            followers = set()
        for tweet in tweets:
            if tweet[0] == user or tweet[0] in followers:
                simulation.append(format_tweet(tweet))
    return simulation

if __name__ == '__main__':
    try:
        user_file = sys.argv[1]
        tweet_file = sys.argv[2]
    except IOError:
        print('Wrong number of arguments.')
    users = get_users(user_file)
    user_followers_mapping = get_user_followers_mapping(user_file)
    tweets = get_tweets(tweet_file)
    simulation = get_simulation(users, user_followers_mapping, tweets)
    for entry in simulation:
        print(entry)
