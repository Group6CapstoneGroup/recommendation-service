# Recommendation Service Setup

## Tools & Prerequisites

- Flask
- PyCharm(IDE)
- CORs
- Postman (Testing purposes only)

## Setup

- First we need to clone down this recommendation-service repository locally on our machine.
- Once we have the repository successfully cloned we can open Pycharm and navigate to our repository.
- In PyCharm open the src folder which contains the python files and csv data set we will need for our application.
- Once we have successfully opened our src folder in pycharm we need to set our enviornment variables.
- Open a terminal window within PyCharm and run the following commands:
- `set FLASK_APP=recommendationService.py`
- `$env:FLASK_APP = "recommendationService.py"`
- `set FLASK_ENV=development`
- `$env:FLASK_ENV = "development"`

If you're on a Mac the commands will be a little different to set the enviornment variables:

- `export FLASK_APP=recommendationService.py`
- `export FLASK_ENV=development`

Once your enviornment variables are successfully set run the following command to launch your application on port 9999 (this is important because the tests are testing against this specific port number):

- `python -m flask run -p 9999`

To verify that you are successfully connected please click this [link](http://127.0.0.1:9999/recommendation) you should see the following output if you successfully launched the web app:

success response from GET call

For a detailed video demo of the setup instructions please click [here](https://www.youtube.com/watch?v=Xwsb9nwrWtg).

## Recommendation Model

### Euclidean-distance

Euclidean distance is being used to calculate which songs are closest to the user input. Euclidean distance is the unit of measurement used in machine learning models such as KNN for determining which points are closest together. Portions of this code have been recycled from the Kaggle notebook listed [here](https://www.kaggle.com/merveeyuboglu/music-recommendation-system-cosine-s/notebook).
