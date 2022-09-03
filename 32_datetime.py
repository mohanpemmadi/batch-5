from datetime import datetime,timedelta,date,time

now = datetime.now()
# print(now)

# my_dt = datetime(2022,9,3,7,44,50)
# print(my_dt)

''' date '''
# today_date = datetime.now().date()
today_date = now.date()

''' time '''
# today_time = datetime.now().time()
today_time = now.time()

# print(today_date)
# print(today_time)

''' year '''

# print(now.year)

''' month '''

# print(now.month)

''' day '''

# print(now.day)

''' hour '''
# print(now.hour)

''' minute '''
# print(now.minute)


''' timedelta '''
now = datetime.now()
print(now)

start = now-timedelta(days=10)
end = now+timedelta(days=10)

# print(start)
# print(end)
print(now+timedelta(hours=5))
print(now+timedelta(minutes=5))
print(now-timedelta(minutes=5))



''' select * from sales where datetime between start and now'''





