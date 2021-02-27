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
          print(curr_time)
          #print(minute)
          if int(hour) == 23 and int(minute) == 59:
               Main.git_tweet()
               print('Git tweet posted')
               time.sleep(60*10)
          elif int(minute) == 30:
               Main.article_tweet()
               print('Article posted')
               time.sleep(60*10)
          else:
               time.sleep(30)
     except KeyboardInterrupt:
          break
