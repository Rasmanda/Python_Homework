#Subtract 5 days days from the current date

import datetime
date_today = datetime.date.today()
date_5_days_ago = date_today - datetime.\
    timedelta(days = 5)
print("By subtracting from today`s date it was", date_5_days_ago, "five days ago.")