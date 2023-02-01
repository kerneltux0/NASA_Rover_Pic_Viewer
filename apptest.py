import unittest
import os

from lib.backend import get_img

class TestAPIResponse(unittest.TestCase):
    
    def test_api_response(self):
        date = "2022-12-01"
        rover = "curiosity"
        api_key = " "
        data_entry = get_img(api_key, date, rover)
        self.assertEqual(data_entry['error']['code'], "API_KEY_INVALID")
    
    def test_backend_return(self):
        api_key = os.path.join( os.getcwd(), 'api_key.txt' )
        date = "2022-12-01"
        rover = "curiosity"
        data_entry = get_img(api_key, date, rover)
        leading = data_entry[0][0:4]
        trailing = data_entry[0][-3:]
        self.assertEqual(leading,"https")
        self.assertEqual(trailing,"JPG")

if __name__ == '__main__':
        unittest.main()