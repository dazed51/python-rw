#!/usr/bin/python

#flask app test

#import the flask class from the flask  q

from flask import Flask

#create the app object

app = Flask(__name__)

#use  the decorator pattern to link the view fucntion to a url

@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string
def hello_world():
    return "hello, world!?!?!?!"

#dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

#dynamic route w/explicit status codes
@app.route("/name/<name>")
def index(name):
    if name.lower() == "david" :
        return "hello, {}".format(name)
    else:
        return "not found", 404

#start the dev server using the run() methods

if __name__ == "__main__":
    app.run()
