## 2. Introduction to the data ##

import pandas as pd
dc_listings=pd.read_csv('dc_airbnb.csv')
print(dc_listings.head(1))

## 4. Euclidean distance ##

import numpy as np
first_distance = np.abs(3 - dc_listings.iloc[0]['accommodates'])
print(first_distance)

## 5. Calculate distance for all observations ##

import numpy as np

def euclidean(row):
    dist = np.abs(3 - row['accommodates'])
    return dist

dc_listings['distance']=dc_listings.apply(euclidean,axis=1)
print(dc_listings['distance'].value_counts())

## 6. Randomizing, and sorting ##

import numpy as np
np.random.seed(1)
arr=np.random.permutation(len(dc_listings))
dc_listings=dc_listings.loc[arr]
dc_listings=dc_listings.sort_values('distance')

## 7. Average price ##

stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollar = stripped_commas.str.replace('$', '')
dc_listings['price']=stripped_dollar.astype('float')
mean_price=dc_listings.iloc[0:5]['price'].mean()

## 8. Function to make predictions ##

# Brought along the changes we made to the `dc_listings` Dataframe.
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

def predict_price(new_listing):
    temp_df = dc_listings.copy()
     ## Complete the function.
    temp_df['distance']=temp_df['accommodates'].apply(lambda x: np.abs(x-new_listing))
    temp_df=temp_df.sort_values('distance')
    predict_price =temp_df.iloc[0:5]['price'].mean()
    
    return(predict_price)

acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)