import requests
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
from flair.models import SequenceTagger
from flair.data import Sentence
import pytesseract
import pyrebase
from pytesseract import Output
import torch
import PIL.Image
import requests
from fastai import *
from fastai.vision import *
import numpy as np


APP = Flask(__name__)
API = Api(APP)
CORS(APP)


#Configuration information for Firebase connection
CONFIG = {
    'apiKey': 'AIzaSyCrQrzpGmwxtICzplBfV4kFw02CYPYHxdc',
    'authDomain': 'hmc-transcribers.firebaseapp.com',
    'databaseURL': 'https://hmc-transcribers.firebaseio.com',
    'projectId': 'hmc-transcribers',
    'storageBucket': 'hmc-transcribers.appspot.com',
    'messagingSenderId': '859954806298'
}


#Create References to Firebase Cloud Storage
FIREBASE = pyrebase.initialize_app(CONFIG)
STORAGE = FIREBASE.storage()
DATABASE = FIREBASE.database()


#Loads in codes.txt which maps an image segmentation pixel prediction to a field
with open('codes.txt' ,'r') as rf:
    count = 0
    CODE_DICT = {}
    for row in rf:
        CODE_DICT.update({count:row.replace('\n','')})
        count+=1

#List of all fields which can be predicted
ALL_FIELDS = [CODE_DICT[i] for i in CODE_DICT if CODE_DICT[i] != 'Void']

#Metric used to calculate image segmentation accuracy during tests
#Required to be defined in order for model to be loaded
def acc_camvid(input, target):
    target = target.squeeze(1)
    mask = target != void_code
    return (input.argmax(dim=1)[mask]==target[mask]).float().mean()


#Load in Image Segmentation Model
LEARN = load_learner(Path('./'))
LEARN.data.single_ds.tfmargs['size'] = None

#Load in Text Clasfication Model
TEXT_MODEL = SequenceTagger.load_from_file('best-model.pt')



def download_image(image_name):
    """
    Returns image from firebase storage.
    """
    image_url = STORAGE.child('cards/'+ image_name).get_url(None)
    img = PIL.Image.open(requests.get(image_url, stream=True).raw)
    img_fastai = open_image(requests.get(image_url, stream=True).raw)
    return img, img_fastai


def run_ocr(image):
    """
    Runs OCR on given image and returns output with no
    newline, comma, or bar character. If OCR returns no
    output, then return that image is unreadable.
    """
    # Define config parameters
    configs = ('-l eng --oem 1 --psm 3')
    # Run tesseract OCR on image
    output_text = pytesseract.image_to_string(image, config=configs)
    text = ''
    for i, char in enumerate(output_text):
        i = i   # Just here to get rid of warnings
        if char == '\n' or char == ',' or char == '|':
            text += ' '
        else:
            text += char
    readable = True
    text_boxes = pytesseract.image_to_data(image, output_type=Output.DICT, config=configs)
    try:
        sentence = Sentence(text)
    except Exception as ocr_error:
        print(ocr_error)
        readable = False
    return sentence, readable, text_boxes


def quick_resize(fastai_image):
    """
    Quick resize of the fastai image type glitch that for some reason doesn't like odd dimensions.
    """
    height, width = fastai_image.size
    if height%2 != 0:
        fastai_image = fastai_image.crop((0,0, height-1, width))
    height, width = fastai_image.size
    if width%2 != 0:
        fastai_image = fastai_image.crop((0,0, height, width-1))
    return fastai_image


def image_seg(fastai_image, text_boxes):
    """
    Funtion to create predictions using the image segmentation model
    """
    try:
        out = LEARN.predict(fastai_image)
        #This turns out into a list of list for easier transversal
        learn_output = out[0].data[0].tolist()
        OCR_boxes = []
        for i in range(len(text_boxes['level'])):
          if text_boxes['conf'][i] != '-1' and text_boxes['text'][i] != '':
            OCR_boxes.append([text_boxes['text'][i], text_boxes['left'][i],
            text_boxes['top'][i], text_boxes['width'][i], text_boxes['height'][i]])
        predictions = {}

        for box in OCR_boxes:
            text = box[0]
            left = box[1]
            top = box[2]
            width = box[3]
            height = box[4]

            ratio_list = [0 for i in CODE_DICT]
            count = 0
            for x in range(left, left+width):
                for y in range(top, top+height):
                  count += 1
                  index = learn_output[y][x]
                  ratio_list[index] += 1

            ratio_dict = {CODE_DICT[i]: float(ratio_list[i])/float(count) for i in range(len(ratio_list))}
            predictions[text] = ratio_dict

        non_void = {}
        for text in predictions:
          if predictions[text]['Void'] != 1.0:
            del predictions[text]['Void']
            non_void[text] = predictions[text]

        seg_predictions = {CODE_DICT[i]:'' for i in CODE_DICT if CODE_DICT[i] != 'Void'}
        for field in ALL_FIELDS:
            best_confidnece = 0.0
            best_text = ''
            for text in non_void:
                if best_confidnece < non_void[text][field]:
                    best_confidnece = non_void[text][field]
                    best_text = text
            seg_predictions[field] = [best_text, best_confidnece]
    except Exception as e:
        return 'Unable to predict!'
    return seg_predictions


def check_input(sentence: Sentence):
    """
    Checks for common problems with the OCR and ML model and aims to fix them
    """
    phone_sigs = ['cell','Cell','phone','Phone','Phone/fax','phone/fax','Phone/Fax']
    fax_sigs =  ['Fax','fax']
    has_email = False
    
    for i,token in enumerate(sentence):
        # Double checking that email address is valid
        if 'email_id' in token.get_tag('ner').value:
            # If no @ symbol, definitely not an email
            if '@' not in token.text:
                token.add_tag('ner','')
            elif not has_email:
                has_email = True

        
        # If no tagged email address, manually tag if conditions are met
        if '@' in token.text and '.' in token.text:
            # first character can't be @ symbol, is likely twitter handle
            if token.text[0] != '@' and not has_email:
                token.add_tag('ner','S-email_id',0.9)

        if token != sentence[-1]:
            # Look for signifiers that next word is a phone number
            for word in phone_sigs:
                if word in token.text:
                    token.add_tag('ner','')
                    if len(sentence[i+1].text) > 9:
                        sentence[i+1].add_tag('ner','S-phone')

            # Look for signifiers that next word is a fax number
            for word in fax_sigs:
                if word in token.text:
                    token.add_tag('ner','')
                    if len(sentence[i+1].text) > 9:
                            sentence[i+1].add_tag('ner','S-fax')
            
        # Check for 5-digit number (zipcode)
        if len(token.text) == 5 and token.text.isdigit():
            token.add_tag('ner','S-zipcode',0.9)


def text_class(scrape, finish):
    """
    Creates predictions using our text classification model
    """
    #text classification model alters sentance by adding prediction tags
    TEXT_MODEL.predict(scrape)
    check_input(scrape)
    fields = []
    for span in scrape.get_spans('ner'):
        fields.append(span.to_dict())
    #gets most confident prediction for each field
    for dictionary in fields:
        if dictionary['type'] in finish:
            if dictionary['confidence'] > finish[dictionary['type']][1]:
                finish[dictionary['type']] = [dictionary['text'], dictionary['confidence']]
        else:
            finish[dictionary['type']] = [dictionary['text'], dictionary['confidence']]
    return finish


@APP.route('/transcribe', methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def run_model():
    """
    Returns JSON of most-confident predictions made by text classification model.
    Gets image name argument from url api call.
    """
    #get image file name from url arguments
    args = request.args
    image_name = args['name']

    if request.method == 'GET':
        image, fastai_image = download_image(image_name)
        scrape, readable, text_boxes = run_ocr(image)
        finish = {}
        fastai_image = quick_resize(fastai_image)

        if readable:
            seg_predictions = image_seg(fastai_image, text_boxes)
            class_predictions = text_class(scrape, finish)

            for field in seg_predictions:
                if field not in class_predictions:
                    class_predictions[field] = seg_predictions[field]
            return jsonify(class_predictions)
        else:
            finish = 'Unable to read!'
            return jsonify(finish)


@APP.route('/')
def testing():
    """
    Home route for testing purposes.
    """
    return 'It works!'


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8000, debug=True)
