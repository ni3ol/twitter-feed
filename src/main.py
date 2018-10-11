user_followers_mapping = {
    'Ward': ['Martin', 'Alan'],
    'Alan': ['Martin'],
 }

tweets = [
    ('Alan', 'If you have a procedure with 10 parameters, you probably missed some.'),
    ('Ward', 'There are only two hard things in Computer Science: cache invalidation, naming things and off-by-1 errors.'),
    ('Alan', 'Random numbers should not be generated with a method chosen at random.'),
]

def get_users_from_user_followers_mapping(user_followers_mapping):
    users = []
    for user, followers in user_followers_mapping.items():
        if user not in users:
            users.append(user)
        for follower in followers:
            if follower not in users:
                users.append(follower)
    return users

def get_users_tweets(user, user_followers_mapping, tweets):
    followers = user_followers_mapping[user]
    user_tweets = []
    for tweet in tweets:
        author = tweet[0]
        if author in followers or author == user:
            user_tweets.append(tweet)
    return user_tweets

def format_tweet(tweet):
    return '@{}: {}'.format(tweet[0], tweet[1])
