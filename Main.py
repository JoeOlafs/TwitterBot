import twitter
import os
import info
#import ArticleInfo

api = twitter.Api(consumer_key=os.environ.get('TwitterAPIKey'),
                    consumer_secret=os.environ.get('TwitterAPISecretKey'),
                    access_token_key=os.environ.get('TwitterAccessToken'),
                    access_token_secret=os.environ.get('TwitterAccessTokenSecret'))

def git_tweet():
     with open('day.txt', 'r') as file:
          day = file.read()
     dayNum = int(day)

     GitContribution = info.gitInfo()
     if GitContribution == 0:
          nextDay = 1
          tweet = f"No contributions made to my Github profile today, guess I'll start #100DaysOfCode Again tomorrow @freeCodeCamp #freeCodeCamp @_100DaysOfCode"
     else:
          nextDay = dayNum + 1
          day = day.replace(day, str(nextDay))
          tweet =   f"#Day{dayNum} of #100DaysofCode Challenge\nI made {GitContribution} contributions to my @Github profile today. Sent out with my #TwitterBot\n#freeCodeCamp #CodeNewbie @freeCodeCamp @_100DaysOfCode"

     api.PostUpdate(tweet)


     with open('day.txt', 'w') as file:
          file.write(day)

def article_tweet():

     next_link = 'link'

     if next_link != '':
          tweet = f'Just a quick read for your enjoyment.\nFeatured on @hashnode\n\nSent out from my #TwitterBot\n#hashnode\n {next_link}'
          #api.PostUpdate(tweet)
          #with open('links.txt', 'a') as file:
          #     file.write('\n')
          #     file.write(next_link)
          return tweet
     else:
          results = 'no link available'
          return results