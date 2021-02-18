import twitter
import os
import info

api = twitter.Api(consumer_key=os.environ.get('TwitterAPIKey'),
                    consumer_secret=os.environ.get('TwitterAPISecretKey'),
                    access_token_key=os.environ.get('TwitterAccessToken'),
                    access_token_secret=os.environ.get('TwitterAccessTokenSecret'))


with open('day.txt', 'r') as file:
     day = file.read()
dayNum = int(day)
nextDay = dayNum + 1
day = day.replace(day, str(nextDay))

GitContribution = info.contributionToday

tweet =   f"#Day{dayNum} of #100Days of Code Challenge\nI made {GitContribution} contributions to my Github profile today\nSent out with my #TwitterBot\n#freeCodeCamp @freeCodeCamp @_100DaysOfCode"

api.PostUpdate(tweet)

with open('day.txt', 'w') as file:
     file.write(day)