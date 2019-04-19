from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
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
CORS(app, resources={r"/*": {"origins": "*"}})


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

def downloadImage():
    
    # storage.child("cards/classexnew.jpg").download("downloaded.jpg")
    imageURL = storage.child("cards/classexnew.jpg").get_url(None)
    # image = urllib.request.urlretrieve(imageURL, '001.jpg')
    
    # file = urllib.request.urlretrieve(imageURL, '001.jpg')
    img = Image.open(requests.get(imageURL, stream=True).raw)
    return img

data = {
  "email_id": [
    "courtneymerkel1S5@augustana.edu", 
    0.3716849386692047
  ], 
  "first_name": [
    "Courtney", 
    0.6033658981323242
  ], 
  "last_name": [
    "Merkel", 
    0.9978609681129456
  ], 
  "office_address": [
    "460 N Green St.  Somonauk", 
    0.7969755291938782
  ], 
  "phone": [
    "706-0011", 
    0.4106656014919281
  ], 
  "state": [
    "IL", 
    0.6271725296974182
  ], 
  "title": [
    "60552     EDUCATION", 
    0.5333120673894882
  ]
}

# def push_data():
#     if request.method == 'POST':

# image = downloadImage()

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
    except:
        readable = False
    return text, readable


@app.route('/transcribe', methods=['POST', 'GET'])
def run_model():
    if request.method == 'GET':
        # model = SequenceTagger.load_from_file('final-model.pt')#database.child("model/best-model.pt")
        # image = downloadImage()
        image = Image.open('000983.jpg')
        scrape, readable = run_OCR(image)
        finish = {}
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
        # jsonify(scrape.to_tagged_string())

if __name__=="__main__":
    app.run(port=5000, debug=True)
