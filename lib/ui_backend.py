from datetime import date
import random

def year_generator(yr_low,yr_high):
    year = random.randint(yr_low,yr_high)
    return year

def month_day():
    today = date.today()
    month = today.strftime('%m')
    day = today.strftime('%d')
    on_this_day = month + day
    return on_this_day