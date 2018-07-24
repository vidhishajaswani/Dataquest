## 1. Recap ##

import pandas as pd
train_df=pd.read_csv('dc_airbnb_train.csv')
test_df=pd.read_csv('dc_airbnb_test.csv')

## 2. Hyperparameter optimization ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

hyper_params=[1,2,3,4,5]
mse_values=[]
for hp in hyper_params:
    knn=KNeighborsRegressor(n_neighbors=hp,algorithm='brute')
    knn.fit(train_df[['accommodates','bedrooms','bathrooms','number_of_reviews']],train_df['price'])
    predictions=knn.predict(test_df[['accommodates','bedrooms','bathrooms','number_of_reviews']])
    mse_values.append(mean_squared_error(test_df['price'],predictions))
    

## 3. Expanding grid search ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

hyper_params=[x for x in range(1, 21)]
mse_values=[]
for hp in hyper_params:
    knn=KNeighborsRegressor(n_neighbors=hp,algorithm='brute')
    knn.fit(train_df[['accommodates','bedrooms','bathrooms','number_of_reviews']],train_df['price'])
    predictions=knn.predict(test_df[['accommodates','bedrooms','bathrooms','number_of_reviews']])
    mse_values.append(mean_squared_error(test_df['price'],predictions))
    

## 4. Visualizing hyperparameter values ##

import matplotlib.pyplot as plt
%matplotlib inline

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
hyper_params = [x for x in range(1, 21)]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)
    
plt.scatter(hyper_params, mse_values)

## 5. Varying features and hyperparameters ##


features = train_df.columns.tolist()
features.remove('price')

hyper_params = [x for x in range(1, 21)]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)

## 6. Practice the workflow ##

two_features = ['accommodates', 'bathrooms']
three_features = ['accommodates', 'bathrooms', 'bedrooms']
hyper_params = [x for x in range(1,21)]
# Append the first model's MSE values to this list.
two_mse_values = list()
# Append the second model's MSE values to this list.
three_mse_values = list()
two_hyp_mse = dict()
three_hyp_mse = dict()

for k in hyper_params:
    knn=KNeighborsRegressor(n_neighbors=k,algorithm='brute')
    knn.fit(train_df[two_features],train_df['price'])
    pred=knn.predict(test_df[two_features])
    mse=mean_squared_error(test_df['price'],pred)
    two_mse_values.append(mse)

two_lowest_mse = two_mse_values[0]
two_lowest_k = 1

for k,mse in enumerate(two_mse_values):
    if mse < two_lowest_mse:
        two_lowest_mse = mse
        two_lowest_k = k + 1
    
for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[three_features], train_df['price'])
    predictions = knn.predict(test_df[three_features])
    mse = mean_squared_error(test_df['price'], predictions)
    three_mse_values.append(mse)
    
three_lowest_mse = three_mse_values[0]
three_lowest_k = 1

for k,mse in enumerate(three_mse_values):
    if mse < three_lowest_mse:
        three_lowest_mse = mse
        three_lowest_k = k + 1

two_hyp_mse[two_lowest_k] = two_lowest_mse
three_hyp_mse[three_lowest_k] = three_lowest_mse

