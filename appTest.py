import unittest
# from app import *
import app
import PIL
from flair.data import Sentence, Token

class api_unit_tests(unittest.TestCase):
    """
    I could totally be doing this wrong so let me know if this is not what we 
    are supposed to be doing. I'm just trying to get a framework for unit 
    testing set up here.
    """

    def test_download_the_image(self):
        """
        Test for download_the_image function
        """
        img_name = '000983.jpg'
        return_val = app.download_the_image(img_name)
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
        phone_sigs = ['cell', 'Cell', 'phone', 'Phone', 'Phone/fax', 'phone/fax', 'Phone/Fax']
        fax_sigs = ['Fax', 'fax']
        
        # Check for email address
        sentence = Sentence()
        token = Token('hello')
        tag = 'S-email_id'
        token.add_tag('ner', tag)
        sentence.add_token(token)
        app.check_input(sentence)
        return_val = sentence[0].get_tag('ner')
        self.assertNotEqual(return_val,tag)

        # Check for phone number
        for sig in phone_sigs:
            sentence = Sentence()
            token = Token(sig)
            tag = 'S-phone'
            token.add_tag('ner', tag)
            app.check_input(sentence)
            return_val = sentence[0].get_tag('ner')
            self.assertNotEqual(return_val,tag)

            token = Token('123-456-7890')
            app.check_input(sentence)
            return_val = sentence[1].get_tag('ner')
            self.assertEqual(return_val,tag)


        # Check for fax number
        for sig in fax_sigs:
            sentence = Sentence()
            token = Token('Fax')
            tag = 'S-fax'
            token.add_tag('ner', tag)
            app.check_input(sentence)
            return_val = sentence[0].get_tag('ner')
            self.assertNotEqual(return_val,tag)
            
            token = Token('123-456-7890')
            app.check_input(sentence)
            return_val = sentence[1].get_tag('ner')
            self.assertEqual(return_val,tag)

        # Check for zipcode
        num = ''
        for i in range(10):
            num+=str(i)
            sentence = Sentence()
            token = Token('12345')
            tag = 'S-zipcode'
            token.add_tag('ner', tag)
            app.check_input(sentence)
            return_val = sentence[0].get_tag('ner')
            if len(num) == 5:
                self.assertEqual(return_val,tag)
            else:
                self.assertNotEqual(return_val,tag)        

if __name__ == '__main__':
    unittest.main()