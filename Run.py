from datetime import datetime
import time
import Main

print('TwitterBot is running')
print('Next tweet will be at 23:55')
while True: 
     try:
          now = datetime.now()
          curr_time = now.strftime("%H:%M:%S")
          var = curr_time.split(':')
          hour = var[0]
          minute = var[1]
          
          if int(hour) == 23 and int(minute) == 55:
               Main.git_tweet()
               print('Git tweet posted:\n' + Main.tweet)
               time.sleep(60*10)
     except KeyboardInterrupt:
          break
