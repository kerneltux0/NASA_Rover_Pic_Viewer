import unittest

from lib.backend import get_img

class TestAPIResponse(unittest.TestCase):
    
    def test_api_response(self):
        date = "2022-12-01"
        rover = "curiosity"
        api_key = " "
        data_entry = get_img(api_key, date, rover)
        self.assertEqual(data_entry['error']['code'], "API_KEY_INVALID")

if __name__ == '__main__':
        unittest.main()