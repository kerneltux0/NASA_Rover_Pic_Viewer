import unittest

from lib.backend import get_img

def test_api_response(self):
    api_key = " "
    date = "2022-12-01"
    rover = "curiosity"
    data_entry = get_img(api_key, date, rover)
    self.assertEqual(data_entry['error']['code'], "API_KEY_INVALID")