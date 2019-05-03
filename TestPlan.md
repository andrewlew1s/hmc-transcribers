# Test Plan

### 1. Introduction
This document provides an general overview of the testing performed on different components of the app. The scope of testing will first be qualifed and then various types of tests performed will be presented in testing strategy. Additionally, for contributors to the repo, the environment where tests should be run and a step by step schedule for those tests will be articulated.

### 2. Scope
This app consists of two main components: a front-end composed of a collection of .vue files and the API used by the front-end to obtain transcription results, which is contained entirely in app.py. For the front end, testing will consist of user testing any changes to verify functionality hasn't been distrupted. For the API, unit test will be performed on all functions defined within the module and integration testing will be performed through calls to API endpoints.

### 3. Testing Strategy
#### 3.1 Unit Testing
Unit tests on any function ought to cover all of the following applicable areas: return type, performance on valid and invalid input, and edge cases concerning loop conditions. Exisiting unit tests are in appTest.py and those test can be run with the following command:
```bash
pipenv shell python appTest.py
```
#### 3.2 Integration Testing
Integration testing, namely the integration of the front-end and API, occurs through making sample requests to the endpoint of our API. Those requests will be performed using the Python library, requests, in the file apiTest.py. While this does not test calls to the API in the exact same manner as they are made by the front-end, this provides an oppurtunity to perform an initial assessment of performance of the API in a consistent and programatic way, rather than through the GUI. Testing the API by making requests using axios, the node module used to make API requests in the front-end, will occur during user testing.

Integration tests can be run with the following command:
```bash
pipenv shell python apiTest.py
```
#### 3.3 User Testing
User testing's ultimate goal to ensure that the functionality of the entire webapp has not been distrupted by changes directly to the front-end or to the API. In its nature, this form of testing is not progamatic and less structured. At a minimum, a contributor should ensure that all pages, homepage, about, and results, render and then attempt to transcribe a valid business card, an image without text, and a non-image file and ensure that expected behavior occurs. This behavior is respectively, transcription results appear, a no text found error is returned, and invalid image type error is returned.

### 4. Testing Environment
The API is deployed on an Amazon web services EC2 machine running Ubuntu 18.4 (Bionic Beaver). 
Testing performed on Ubuntu 10 bioinc 18.4 amd64 someone look this up
### 5. Testing Schedule
For front-end commits:

For back-end commits:
