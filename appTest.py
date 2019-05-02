import unittest
from app import *
# import app
import PIL

class api_test(unittest.TestCase):
    """
    I could totally be doing this wrong so let me know if this is not what we 
    are supposed to be doing. I'm just trying to get a framework for unit 
    testing set up here.
    """
    def test_download_image(self):
        """
        Test for download_image function
        """
        img_name = "000983.jpg"
        return_val = download_image(img_name)
        typeof_pic = PIL.JpegImagePlugin.JpegImageFile
        self.assertIsInstance(return_val, typeof_pic)

    def test_run_ocr(self):
        """
        Test for run_ocr function
        """
        self.assertTrue(True)   # Placeholder

    def test_run_model(self):
        """
        Test for run_model function
        """
        self.assertTrue(True)   # Placeholder

    def test_check_input(self):
        """
        Test for check_input function
        """
        self.assertTrue(True)   # Placeholder

if __name__ == '__main__':
    unittest.main()