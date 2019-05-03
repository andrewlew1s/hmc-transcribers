import unittest
import app
import PIL
from flair.data import Sentence, Token

class api_unit_tests(unittest.TestCase):
    """
    Unit tests for app.py
    """

    def test_download_the_image(self):
        """
        Test for download_the_image function
        """
        img_name = '000983.jpg'
        return_val, unused_image = app.download_the_image(img_name)
        typeof_pic = PIL.JpegImagePlugin.JpegImageFile
        self.assertIsInstance(return_val, typeof_pic)

    def test_run_ocr(self):
        """
        Test for run_ocr function
        """
        img_name = '000983.jpg'
        return_image, unused_image = app.download_the_image(img_name)
        text, readable, unused_text_boxes = app.run_ocr(return_image) 
        self.assertTrue(readable)
        self.assertTrue(text != '')

    def test_run_model(self):
        """
        Test for run_model function (Not testable w/out API call)
        """
        self.assertTrue(True)   # Placeholder

        
    def test_image_seg(self):
        """
        Test for image_seg function
        """
        # This image fails to be predicted by the image seg model
        img_name = '000004.jpg'
        test_image, bad_image = app.download_the_image(img_name)
        unused_text, readable, text_boxes = app.run_ocr(test_image)
        seg_predictions, predictability = app.image_seg(test_image, text_boxes)

        self.assertIsNotNone(bad_image)
        self.assertTrue(readable)
        self.assertFalse(predictability)
        self.assertEqual(seg_predictions, 'Unable to predict.')

        
    def test_quick_resize(self):
        """
        Test for quick_resize function
        """
        #getting proper image and image type
        #testing image that will not be resized
        img_name = '000983.jpg'
        unused_image, test_image = app.download_the_image(img_name)
        height_test, width_test = test_image.size
        return_imgae = app.quick_resize(test_image)
        height_return, width_return = return_imgae.size
        self.assertTrue([height_test, width_test] == [height_return, width_return])

        #getting proper image and image type
        #testing image that will be resized
        img_name = '000001.jpg'
        unused_image, test_image = app.download_the_image(img_name)
        height_test, width_test = test_image.size
        return_imgae = app.quick_resize(test_image)
        height_return, width_return = test_image.size
        self.assertFalse([height_test, width_test] == [height_return, width_return])

    def test_text_class(self):
        """
        Test for text_class function
        """
        test_sentence = Sentence('Lavon Burgo 411 High Street, Randolph, MA 02368')
        predictions = app.text_class(test_sentence, {})
        print(predictions)

        self.assertTrue(predictions['state'][0] == 'MA')
        self.assertTrue(predictions['zipcode'][0] == '02368')

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
        return_val = sentence[0].get_tag('ner').value
        self.assertNotEqual(return_val,tag)

        token = Token('hello@world.com')
        sentence.add_token(token)
        app.check_input(sentence)
        return_val = sentence[1].get_tag('ner').value
        self.assertEqual(return_val,tag)

        token = Token('hello2@world.com')
        sentence.add_token(token)
        app.check_input(sentence)
        return_val = sentence[2].get_tag('ner').value
        self.assertNotEqual(return_val,tag)

        # Check for phone number
        for sig in phone_sigs:
            sentence = Sentence()
            token = Token(sig)
            tag = 'S-phone'
            token.add_tag('ner', tag)
            sentence.add_token(token)
            token = Token('123-456-7890')
            sentence.add_token(token)
            app.check_input(sentence)
            return_val = sentence[0].get_tag('ner').value
            self.assertNotEqual(return_val,tag)
            return_val = sentence[1].get_tag('ner').value
            self.assertEqual(return_val,tag)


        # Check for fax number
        for sig in fax_sigs:
            sentence = Sentence()
            token = Token(sig)
            tag = 'S-fax'
            token.add_tag('ner', tag)
            sentence.add_token(token)
            token = Token('123-456-7890')
            sentence.add_token(token)
            app.check_input(sentence)
            return_val = sentence[0].get_tag('ner').value
            self.assertNotEqual(return_val,tag)
            return_val = sentence[1].get_tag('ner').value
            self.assertEqual(return_val,tag)

        # Check for zipcode
        num = ''
        for i in range(10):
            num+=str(i)
            sentence = Sentence()
            token = Token(num)
            tag = 'S-zipcode'
            sentence.add_token(token)
            app.check_input(sentence)
            return_val = sentence[0].get_tag('ner').value
            if len(num) == 5:
                self.assertEqual(return_val,tag)
            else:
                self.assertNotEqual(return_val,tag)        

if __name__ == '__main__':
    unittest.main()
