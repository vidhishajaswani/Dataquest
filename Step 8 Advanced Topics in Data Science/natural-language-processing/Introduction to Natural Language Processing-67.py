## 2. Overview of the Data ##

import pandas as pd
submissions = pd.read_csv("sel_hn_stories.csv")
submissions.columns = ["submission_time", "upvotes", "url", "headline"]
submissions = submissions.dropna()

## 3. Tokenizing the Headlines ##

tokenized_headlines = []
for item in submissions["headline"]:
    tokenized_headlines.append(item.split())

## 4. Preprocessing Tokens to Increase Accuracy ##

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []
for item in tokenized_headlines:
    tokens = []
    for token in item:
        token = token.lower()
        for punc in punctuation:
            token = token.replace(punc, "")
        tokens.append(token)
    clean_tokenized.append(tokens)

## 5. Assembling a Matrix of Unique Words ##

import numpy as np
unique_tokens = []
single_tokens = []

for each in clean_tokenized:
    for token in each:
        if token not in single_tokens:
            single_tokens.append(token)
        elif token in single_tokens and token not in unique_tokens:
            unique_tokens.append(token)
        
        
counts=pd.DataFrame(0, index=np.arange(len(clean_tokenized)), columns=unique_tokens)

## 6. Counting Token Occurrences ##

# We've already loaded in clean_tokenized and counts
for i, item in enumerate(clean_tokenized):
    for token in item:
        if token in unique_tokens:
            counts.iloc[i][token] += 1

## 7. Removing Columns to Increase Accuracy ##

# We've already loaded in clean_tokenized and counts
word_counts = counts.sum(axis=0)

counts = counts.loc[:,(word_counts >= 5) & (word_counts <= 100)]

## 8. Splitting the Data Into Train and Test Sets ##

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(counts, submissions["upvotes"], test_size=0.2, random_state=1)

## 9. Making Predictions With fit() ##

from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(X_train,y_train)
predictions=clf.predict(X_test)

## 10. Calculating Prediction Error ##

mse=((predictions-y_test)**2).sum()/len(predictions)