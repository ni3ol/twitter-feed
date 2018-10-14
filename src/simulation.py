from tweet_handler import TweetHandler

class Simulation(object):
    def get_simulation(self, users, user_followers_mapping, tweets):
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
                    simulation.append(TweetHandler().format_tweet(tweet))
        return simulation