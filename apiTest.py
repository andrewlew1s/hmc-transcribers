import os
import requests
import unittest
import app
import PIL
from flair.data import Sentence, Token

os.environ['NO_PROXY'] = '0.0.0.0'

class api_unit_tests(unittest.TestCase):
    def test_valid_image_test(self):
        r = requests.get('http://localhost:8000/transcribe?name=000983.jpg')
        json_r = r.json()
        self.assertTrue(json_r['first_name']=='Courtney')

    def test_invalid_image_test(self):
        r = requests.get('http://localhost:8000/transcribe?name=IMG_0414.jpg')
        response = r.content
        self.assertTrue(response=='Unable to read.')


    def test_not_image_test(self):
        r = requests.get('http://localhost:8000/transcribe?name=000983')
        response = r.content
        self.assertTrue(response=='File name does not exist.')

if  __name__ == '__main__':
    unittest.main()
