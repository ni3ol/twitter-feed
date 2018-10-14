import sys
from tweet_handler import TweetHandler
from user_parser import UserParser
from tweet_parser import TweetParser
from simulation import Simulation


if __name__ == '__main__':
    try:
        user_file = sys.argv[1]
        tweet_file = sys.argv[2]
    except:
        print('Wrong number of arguments.')
    user_parser = UserParser()
    tweet_parser = TweetParser()
    user_tweet_simulation = Simulation() 

    users = user_parser.get_users(user_file)
    user_followers_mapping = user_parser.get_user_followers_mapping(user_file)
    tweets = tweet_parser.get_tweets(tweet_file)
    simulation = user_tweet_simulation.get_simulation(users, user_followers_mapping, tweets)
    for entry in simulation:
        print(entry)
