import requests
from PIL import Image
from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS, cross_origin
from flair.models import SequenceTagger
from flair.data import Sentence
import pytesseract
import pyrebase

APP = Flask(__name__)
API = Api(APP)
CORS(APP)

#Configuration information for Firebase connection
CONFIG = {
    "apiKey": "AIzaSyCrQrzpGmwxtICzplBfV4kFw02CYPYHxdc",
    "authDomain": "hmc-transcribers.firebaseapp.com",
    "databaseURL": "https://hmc-transcribers.firebaseio.com",
    "projectId": "hmc-transcribers",
    "storageBucket": "hmc-transcribers.appspot.com",
    "messagingSenderId": "859954806298"
}

#Create References to Firebase Cloud Storage
FIREBASE = pyrebase.initialize_app(CONFIG)
STORAGE = FIREBASE.storage()
DATABASE = FIREBASE.database()

#Load in Text Clasfication Model
TEXT_MODEL = SequenceTagger.load_from_file("gurt-model.pt")

def download_image(image_name):
    '''
    Returns image from firebase storage.
    '''
    image_url = STORAGE.child("cards/"+ image_name).get_url(None)
    img = Image.open(requests.get(image_url, stream=True).raw)
    return img

@APP.route('/')
def testing():
    '''
    Home route for testing purposes.
    '''
    return 'It works!'

def run_ocr(image):
    '''
    Runs OCR on given image and returns output with no
    newline, comma, or bar character. If OCR returns no
    output, then return that image is unreadable.
    '''
    # Define config parameters
    configs = ('-l eng --oem 1 --psm 3')
    # Run tesseract OCR on image
    output_text = pytesseract.image_to_string(image, config=configs)
    text = ''
    for i, char in enumerate(output_text):
        if char == '\n' or char == ',' or char == '|':
            text += ' '
        else:
            text += char
    readable = True
    try:
        text = Sentence(text)
    except Exception as ocr_error:
        print(ocr_error)
        readable = False
    return text, readable

@APP.route('/transcribe', methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def run_model():
    '''
    Returns JSON of most-confident predictions made by text classification model.
    Gets image name argument from url api call.
    '''
    #get image file name from url arguments
    args = request.args
    image_name = args['name']

    if request.method == 'GET':
        image = download_image(image_name)
        scrape, readable = run_ocr(image)
        finish = {}
        if readable:
            #text classification model alters sentance by adding prediction tags 
            TEXT_MODEL.predict(scrape)
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
            return jsonify(finish)
        else:
            finish = 'Unable to read!'
            return jsonify(finish)


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=8000, debug=True)
