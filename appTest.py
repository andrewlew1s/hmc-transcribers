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
        return_val = app.download_the_image(img_name)
        typeof_pic = PIL.JpegImagePlugin.JpegImageFile
        self.assertIsInstance(return_val, typeof_pic)

    def test_run_ocr(self):
        """
        Test for run_ocr function
        """
        #TODO
        self.assertTrue(True)   # Placeholder

    def test_run_model(self):
        """
        Test for run_model function
        """
        #TODO
        self.assertTrue(True)   # Placeholder

    def test_acc_camvid(self):
        """
        Test for the acc_camvid function
        """
        #TODO
        self.assertTrue(True)   # Placeholder

    def test_cross_origin(self):
        """
        Test for <fill this in with function name> function
        """
        #TODO
        self.assertTrue(True)   # Placeholder
        
    def test_image_seg(self):
        """
        Test for <fill this in with function name> function
        """
        #TODO
        self.assertTrue(True)   # Placeholder

    def test_jsonify(self):
        """
        Test for <fill this in with function name> function
        """
        #TODO
        self.assertTrue(True)   # Placeholder
        
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
        height_return, width_return = return_imgae.size
        self.assertFalse([height_test, width_test] == [height_return, width_return])

    def test_text_class(self):
        """
        Test for <text_class> function
        """
        test_sentence = Sentence('Lavon Burgo 411 High Street, Randolph, MA 02368')
        predictions = app.text_class(test_sentence, {})

        self.assertTrue(predictions['state'] == 'MA')
        self.assertTrue(predictions['zipcode'] == '02368')

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

        token = Token('hello@world.com')
        sentence.add_token(token)
        app.check_input(sentence)
        return_val = sentence[1].get_tag('ner')
        self.assertEqual(return_val,tag)

        token = Token('hello2@world.com')
        sentence.add_token(token)
        app.check_input(sentence)
        return_val = sentence[2].get_tag('ner')
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
            token = Token(num)
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
