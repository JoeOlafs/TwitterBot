import twitter
import os
import GitInfo

api = twitter.Api(consumer_key=os.environ.get('TwitterAPIKey'),
                    consumer_secret=os.environ.get('TwitterAPISecretKey'),
                    access_token_key=os.environ.get('TwitterAccessToken'),
                    access_token_secret=os.environ.get('TwitterAccessTokenSecret'))

def git_tweet():
     with open('day.txt', 'r') as file:
          day = file.read()
     dayNum = int(day)

     GitContribution = GitInfo.gitInfo()
     if GitContribution == 0:
          nextDay = 1
          tweet = f"No contributions made to my Github profile today, guess I'll start #100DaysOfCode Again tomorrow @freeCodeCamp #freeCodeCamp @_100DaysOfCode"
     else:
          nextDay = dayNum + 1
          day = day.replace(day, str(nextDay))
          tweet =   f"#Day{dayNum} of #100DaysofCode Challenge\nI made {GitContribution} contributions to my @Github profile today. Sent out with my #TwitterBot\n#freeCodeCamp #CodeNewbie @freeCodeCamp @_100DaysOfCode"

     api.PostUpdate(tweet)

     os.system("Tweet uploaded")
     os.system("Tweet: " + tweet)


     with open('day.txt', 'w') as file:
          file.write(day)