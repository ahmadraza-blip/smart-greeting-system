# "import datetime=>import=bring and datetime=Date&Time module So,It's mean Import the datetime module so Python can use the current date and time"
import datetime
# datetime.datetime.now()=>Gets the current date and time.And,hour=>Gets only the current hour (0-23).Store in hour in the variable hour.
hour=datetime.datetime.now().hour
if hour>=5 and hour<7:
    print("Good Morning")
elif hour>=7 and hour <12:
    print("Good Afternoon")
elif hour>=12 and hour<5:
    print("Good Evening")
else:
    print("Good Night")
# module datetime
import datetime
now=datetime.datetime.now()
print(now)