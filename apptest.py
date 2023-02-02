import unittest
import os

from lib.backend import get_img
from factory import Factory, search_api_imgs

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

    def test_api_search(self):
        api_key_file = os.path.join( os.getcwd(), 'api_key.txt' )
        file = open(api_key_file)
        api_key = file.readline()
        file.close()
        date = "2022-11-01"
        rover = "curiosity"
        data = search_api_imgs(api_key,date,rover)
        self.assertIsInstance(data,Factory)
        self.assertEqual(data.date,date)
        self.assertEqual(data.rover,rover)
        self.assertNotEqual(data.images.count,0)
        

if __name__ == '__main__':
        unittest.main()