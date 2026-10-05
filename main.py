import datetime
hour = datetime.datetime.now().hour
if hour >0 and hour <12:
    print("Good Morning")
elif hour>=12 and hour <17:
    print("Good afternoon")
elif hour >=17 and hour <21:
    print("Good evening")
else:
    print("Good night")
import datetime
current = datetime.datetime.now()
print(current)

import time
current = time.strftime("%H:%M:%S")
print(current)
hour = int(time.strftime("%H"))
if 0 <= hour <12:
    print("Good Morning")
elif 12 <= hour <17:
    print("Good Afternoon")
elif 17 <= hour <21:
    print("Good Evening")
else:
    print("Good Night")
