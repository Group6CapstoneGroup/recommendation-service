import json

from flask import Flask, jsonify, request, render_template, abort, redirect, url_for
from flask_cors import CORS
from main import euclidean_matrix,data


# Each method needs to have a unique name for a web app in flask or it will give you an error.

app = Flask(__name__)
CORS(app)


@app.route('/recommendation', methods=["GET", "POST"])
def recommendations():
    if request.method == "POST":
        # form has been submitted, process data
        print("this is what the request looks like:")

        # this captures json object in variable r
        r = request.data

        # this loads json object into y
        y = json.loads(r)

        # access properties in the json object array
        print(y["track"])

        track, artist = euclidean_matrix(data, 1, y["track"], y["artist"])

        return "Here is your recommendation: " + str(artist) + " " + str(track)
    else:
        return "success response from GET call"
