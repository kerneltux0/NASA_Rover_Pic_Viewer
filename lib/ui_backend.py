from datetime import date
from key_file import get_api_key
from lib.api_query import get_img
import random

def year_generator(yr_low,yr_high):
    year = random.randint(yr_low,yr_high)
    return year

def month_day():
    today = date.today()
    month = today.strftime('%m')
    day = today.strftime('%d')
    on_this_day = month + "-" + day
    return on_this_day

def run_search(date,rover):
    key = get_api_key()
    images = get_img(key,date,rover)
    
