from datetime import datetime
import time
import Main

while True:
     try:
          now = datetime.now()
          curr_time = now.strftime("%H:%M:%S")
          var = curr_time.split(':')
          hour = var[0]
          minute = var[1]
          print('TwitterBot is running')
          print('Next tweet will be at 23:55')
          if int(hour) == 23 and int(minute) == 55:
               Main.git_tweet()
               print('Git tweet posted')
               time.sleep(60*10)
          else:
               time.sleep(60)
     except KeyboardInterrupt:
          break
