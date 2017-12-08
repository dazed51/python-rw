#!/usr/bin/python

#flask app test

#import the flask class from the flask package

from flask import Flask

#create the app object

app = Flask(__name__)

#use  the decorator pattern to link the view fucntion to a url

@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string

def hello_world():
    return "hello world"

#start the dev server using the run() methods

if __name__ == "__main__":
    app.run()
