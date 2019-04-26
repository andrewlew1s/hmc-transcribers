from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
import pyrebase
import pytesseract
import flair
from flair.models import SequenceTagger
from flair.data import Label, Token, Sentence
import torch
from PIL import Image
import requests

app = Flask(__name__)
api = Api(app)
#cors = CORS(app, resources={r"/transcribe": {"origins": "ec2-13-57-16-89.us-west-1.compute.amazonaws.com:8000"}})
CORS(app)

config = {
    "apiKey": "AIzaSyCrQrzpGmwxtICzplBfV4kFw02CYPYHxdc",
    "authDomain": "hmc-transcribers.firebaseapp.com",
    "databaseURL": "https://hmc-transcribers.firebaseio.com",
    "projectId": "hmc-transcribers",
    "storageBucket": "hmc-transcribers.appspot.com",
    "messagingSenderId": "859954806298"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
database = firebase.database()

# modelURL = storage.child("models/final-model.pt").get_url(None)
model = SequenceTagger.load_from_file("final-model.pt")

def downloadImage(imageName):
    
    # storage.child("cards/classexnew.jpg").download("downloaded.jpg")
    imageURL = storage.child("cards/"+ imageName).get_url(None)
    # image = urllib.request.urlretrieve(imageURL, '001.jpg')
    
    # file = urllib.request.urlretrieve(imageURL, '001.jpg')
    img = Image.open(requests.get(imageURL, stream=True).raw)
    return img

# def push_data():
#     if request.method == 'POST':

# image = downloadImage()


@app.route('/')
def testing():
    return 'It works!'


# UI accesses to generated fields
@app.route('/fields', methods=['POST','GET'])
def get_data():
    if request.method == 'GET':
        return jsonify(data)



def run_OCR(image):
    # Define config parameters
    configs = ('-l eng --oem 1 --psm 3')
    # Run tesseract OCR on image
    outputText = pytesseract.image_to_string(image, config=configs)
    text = ''
    for i, char in enumerate(outputText):
        if char == '\n' or char == ',' or char == '|':
            text += ' '
        else:
            text += char
    readable = True
    try:
        text = Sentence(text)
    except Exception as e:
        print(e)
        readable = False
    return text, readable

@app.route('/transcribe', methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def run_model():
    args = request.args
    imageName = args['name']

    if request.method == 'GET':
        # model = SequenceTagger.load_from_file('final-model.pt')#database.child("model/best-model.pt")
        image = downloadImage(imageName)
        #image = Image.open('000983.jpg')
        scrape, readable = run_OCR(image)
        finish = {scrape}
        if readable:
            model.predict(scrape)
            fields = []
            for span in scrape.get_spans('ner'):
                fields.append(span.to_dict())
            for dictionary in fields:
                if dictionary['type'] in finish:
                    if dictionary['confidence'] > finish[dictionary['type']][1]:
                        finish[dictionary['type']] = [dictionary['text'], dictionary['confidence']]
                else:
                    finish[dictionary['type']] = [dictionary['text'], dictionary['confidence']]

            return jsonify(finish)
        else:
            return jsonify('Unable to read!')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
