from datetime import datetime
import time
import Main

while True:
     now = datetime.now()
     curr_time = now.strftime("%H:%M:%S")
     var = curr_time.split(':')
     hour = var[0]
     minute = var[1]
     print(curr_time)
     print(minute)
     if int(hour) == 23 and int(minute) == 59:
          Main.git_tweet()
          time.sleep(60*30)
     else:
          time.sleep(10)
