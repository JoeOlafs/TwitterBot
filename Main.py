import twitter
import os
import info

api = twitter.Api(consumer_key=os.environ.get('TwitterAPIKey'),
                    consumer_secret=os.environ.get('TwitterAPISecretKey'),
                    access_token_key=os.environ.get('TwitterAccessToken'),
                    access_token_secret=os.environ.get('TwitterAccessTokenSecret'))

GitContribution = info.contributionToday