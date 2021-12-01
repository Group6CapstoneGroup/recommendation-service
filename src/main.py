# recommendation-service requirment: 1.0.2 The second is main.py. This file contains the recommendation model.
# Citation:
# https://www.kaggle.com/merveeyuboglu/music-recommendation-system-cosine-s/notebook

# Imports
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from scipy.spatial import distance

import warnings

warnings.filterwarnings("ignore")


# recommendation-service requirement 1.1.0 The recommendation model will first need to open
# and read all the lines of data from the csv file we are utilizing as a database
# for the model to make it's predictions on.
# Import Dataset
data = pd.read_csv('data.csv')
# preview data
data.head()

# recommendation-service requirement 1.1.1 We then need to clean the data so the model
# will be able to digest it and its easier to work with.
# rename some of the columns so they're easier to work with
data.rename(columns={'artist_name': 'Artist', 'track_name': 'Song'}, inplace=True)
# check dataframe again
data.head()

# cleaning up the data a bit, getting rid of columns that are not needed / would be difficult for procecessing
data = data.drop(["track_id", "key", "mode", "time_signature"], 1)
# create a copy of the dataframe
df = data.copy()
# in the new dataframe, drop the columns for artist and song
df = df.drop(["Artist", "Song"], 1)

# normalizing data
song_features = ['popularity', 'acousticness', 'danceability', 'duration_ms',
                 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness',
                 'tempo', 'valence']
scaler = StandardScaler()
df[song_features] = scaler.fit_transform(df[song_features])

# looking at pearson correlation coefficient to see if there is a correlation between features
data.corr()

# using One Hot Encoder to encode genre variables for processing

OHE = OneHotEncoder(sparse=False, handle_unknown="ignore")
encoder = pd.DataFrame(OHE.fit_transform(np.array(df["genre"]).reshape(-1, 1)))
encoder.columns = df["genre"].unique()

df[encoder.columns] = encoder
df = df.drop("genre", 1)
df.head()

# creating a new dataframe with the string values
df["song_name"] = data["Song"]
df["artist_name"] = data["Artist"]

# drop values in new dataframe

df_2 = df.drop(["artist_name", "song_name"], 1)


# this function looks for the user input of the song / artist to see if they exist in the database

def find_song(song, artist):
    a = 0
    b = 0
    for i in data["Song"]:
        if song.lower() in i.lower() and artist.lower() in data["Artist"][a].lower():
            print("Name of Song: ", data["Song"][a], ", Name of Artist: ", data["Artist"][a])
            b += 1
        a += 1
    if b == 0:
        print("404 song and/or artist not found, please try your search again")


# function to find songs similar to the user input

def find_similar_songs(song, artist):
    a = 0
    b = 0
    songs = []
    indexes = []
    for i in data["Song"]:
        if song.lower() in i.lower() and artist.lower() in data["Artist"][a].lower():
            songs.append(df_2[a:a + 1].values)
            indexes.append(a)
            b += 1
        a += 1
    if b == 0:
        print("404 Song and/or Artist not found, please try your search again")
        return 0

    return songs[0][0], indexes[0]


# requirement 1.1.2 The file will also contain a method called
# euclidean_matrix(data, numberOfRecommendations, song, artist). The purpose of this method is call the model
# and get recommendation outputs the model generates from the algorithm it utilizes.
# The inputs that are needed to be passed in are the data itself from the csv file, number of recommendations wanted,
# song title, and artist. The method then returns the printed text of the song recommendation(s) it has made.

# this function will call the find similar songs function and calculate the euclidean distance to determine which songs
# are the closest fit to the user input, thus generating recommendations based on the song and artist
def euclidean_matrix(data, number, song, artist):
    # checking to make sure song/artist exists
    if find_similar_songs(song, artist) == 0:
        return 0
    else:
        x = find_similar_songs(song, artist)[0]
        index = find_similar_songs(song, artist)[1]
    p = []
    count = 0
    # distance.euclidean will calculate the euclidean distance between points to recommend songs that are the closest
    # euc. distance is used in machine learning applications such as knn as the means of determining closeness between
    # points
    for i in df_2.values:
        p.append([distance.euclidean(x, i), count])
        count += 1
    p.sort()
    song_names = df["song_name"]
    artist_names = df["artist_name"]

    print("\nSimilar songs to ", song_names[index], " by ", artist_names[index], "\n")
    for i in range(1, number + 1):
        print(i, "- ", song_names[p[i][1]], ", ", artist_names[p[i][1]])
        a = song_names[p[i][1]]
        b = artist_names[p[i][1]]
    return a, b
