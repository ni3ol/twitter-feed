# Twitter Simulation

## Setup
Install the requirements.
```
pip install -r requirements.txt
```

## Tests
Run the tests.
```
./bin/run-tests.sh
```

## Running the Simulation
- run `./bin/run-program.sh [USER_FILE] [TWEET_FILE]`
- eg. `./bin/run-program.sh ./data/user.txt ./data/tweet.txt`
- tweet and user txt files can be found in the data directory
- the simulation will output to Terminal

## Assumptions
- Each user will see their own tweets as well as the tweets from the users they follow.
- The program takes in 2 filenames that are used to process user and tweet information.
- The program does not take in a continuous stream of data as of thi version.