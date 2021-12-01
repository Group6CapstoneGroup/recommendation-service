# recommendation-service requirement 1.0.3 The third is recommendationService.py.
# This file is where we implement our Flask web app service that communicates with the UI
import json
from flask import Flask, request
from flask_cors import CORS
from main import euclidean_matrix, data


# Each method needs to have a unique name for a web app in flask or it will give you an error.

# recommendation-service requirement 1.2.0 The recommendationService.py file needs
# to first specify that it wants to run as the Flask web application.
app = Flask(__name__)
# recommendation-service requirement 1.2.1 Once we specified this file for our
# web application we need to support CORS by importing it into our application.
CORS(app)


# recommendation-service requirement 1.2.2 We then need to create a API endpoint with the
# specified route: `/recommendations`. This endpoint will handle the POST request and interact with the model.
@app.route('/recommendation', methods=["GET", "POST"])
def recommendations():
    if request.method == "POST":

        # recommendation-service requirement 1.2.3
        # We then will capture the body passed in the request to a variable which loads the json object.
        # this captures json object in variable r
        r = request.data

        # this loads json object into y
        y = json.loads(r)

        # access properties in the json object array
        print(y["track"])

        # recommendation-service requirement 1.2.4 We then pass in the
        # json properties needed to the euclidean_matrix method which are just the track
        # and artist name.
        track, artist = euclidean_matrix(data, 1, y["track"], y["artist"])

        # We then save the response from the method and return back the recommendation to the client.
        # Add in a unique string which is %song% to split up the artist and track.
        return str(artist) + "%song%" + str(track)
    else:
        return "success response from GET call"
