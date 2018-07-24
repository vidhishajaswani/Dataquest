## 1. Introduction to the Data ##

import pandas as pd
nba = pd.read_csv("nba_2013.csv")

# The names of the columns in the data
print(nba.columns.values)

## 3. Finding Similar Rows With Euclidean Distance ##

selected_player = nba[nba["player"] == "LeBron James"].iloc[0]
distance_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']
import math
def get_dist(row):
    inner_value = 0
    for k in distance_columns:
        inner_value += (row[k] - selected_player[k]) ** 2
    return math.sqrt(inner_value)

lebron_distance = nba.apply(get_dist, axis=1)
    

## 4. Normalizing Columns ##

nba_numeric = nba[distance_columns]

mean=nba_numeric.mean()
std=nba_numeric.std()

nba_normalized=(nba_numeric-mean)/std

## 5. Finding the Nearest Neighbor ##

from scipy.spatial import distance

# Fill in the NA values in nba_normalized
nba_normalized.fillna(0, inplace=True)

# Find the normalized vector for Lebron James
lebron_normalized = nba_normalized[nba["player"] == "LeBron James"]

# Find the distance between Lebron James and everyone else.
euclidean_distances = nba_normalized.apply(lambda row: distance.euclidean(row, lebron_normalized), axis=1)
distance_frame = pandas.DataFrame(data={"dist": euclidean_distances, "idx": euclidean_distances.index})
distance_frame.sort_values("dist",inplace=True)
second_smallest=distance_frame.iloc[1]["idx"]
most_similar_to_lebron = nba.loc[int(second_smallest)]["player"]

## 6. Generating Training and Testing Sets ##

import random
from numpy.random import permutation

# Randomly shuffle the index of nba
random_indices = permutation(nba.index)
# Set a cutoff for how many items we want in the test set (in this case 1/3 of the items)
test_cutoff = math.floor(len(nba)/3)
# Generate the test set by taking the first 1/3 of the randomly shuffled indices
test = nba.loc[random_indices[1:test_cutoff]]
# Generate the train set with the rest of the data
train = nba.loc[random_indices[test_cutoff:]]

## 7. Using sklearn ##

# The columns that we'll be using to make predictions
x_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf']
# The column we want to predict
y_column = ["pts"]

from sklearn.neighbors import KNeighborsRegressor
# Create the kNN model
knn = KNeighborsRegressor(n_neighbors=5)
# Fit the model on the training data
knn.fit(train[x_columns], train[y_column])
# Make predictions on the test set using the fit model
predictions = knn.predict(test[x_columns])

## 8. Computing Error ##

actual = test[y_column]
mse=((predictions-actual)**2).sum()/len(actual)