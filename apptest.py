import unittest
import os
from datetime import date

from lib.api_query import get_img
from lib.ui_backend import year_generator, month_day


class TestAPIResponse(unittest.TestCase):
    
    def test_api_response(self):
        date = "2022-12-01"
        rover = "curiosity"
        api_key = " "
        data_entry = get_img(api_key,date,rover)
        self.assertEqual(data_entry['error']['code'], "API_KEY_INVALID")
    
    def test_backend_return(self):
        api_key_file = os.path.join( os.getcwd(), 'api_key.txt' )
        file = open(api_key_file)
        api_key = file.readline()
        file.close()
        date = "2022-12-01"
        rover = "curiosity"
        data_entry = get_img(api_key,date,rover)
        leading = data_entry[0][0:4]
        trailing = data_entry[0][-3:]
        self.assertIn("http",leading)
        self.assertEqual(trailing,"JPG")
    
    def test_year_gen(self):
        year_low = 2002
        year_high = 2020
        test_year = year_generator(year_low,year_high)
        self.assertGreater(test_year,year_low)
        self.assertLess(test_year,year_high)

    def test_on_this_date(self):
        today = date.today()
        month = today.strftime('%m')
        day = today.strftime('%d')
        mon_day = month + day
        odt_gen = month_day()
        self.assertEqual(mon_day,odt_gen)

        
if __name__ == '__main__':
        unittest.main()