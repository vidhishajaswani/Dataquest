## 1. Introduction ##

# Let's say this is your running history for the past week
# For each day, it records whether or not you ran, and whether or not you were tired
days = [["ran", "was tired"], ["ran", "was not tired"], ["didn't run", "was tired"], ["ran", "was tired"], ["didn't run", "was not tired"], ["ran", "was not tired"], ["ran", "was tired"]]

# Let's say we want to use Bayes' theorem to calculate the odds that you were tired, given that you ran
# This is P(A)
prob_tired = len([d for d in days if d[1] == "was tired"]) / len(days)
# This is P(B)
prob_ran = len([d for d in days if d[0] == "ran"]) / len(days)
# This is P(B|A)
prob_ran_given_tired = len([d for d in days if d[0] == "ran" and d[1] == "was tired"]) / len([d for d in days if d[1] == "was tired"])

# Now we can calculate P(A|B)
prob_tired_given_ran = (prob_ran_given_tired * prob_tired) / prob_ran

print("Probability of being tired given that you ran: {0}".format(prob_tired_given_ran))

## 2. Overview of Naive Bayes ##

# Here's our data, but with "woke up early" or "didn't wake up early" added
days = [["ran", "was tired", "woke up early"], ["ran", "was not tired", "didn't wake up early"], ["didn't run", "was tired", "woke up early"], ["ran", "was tired", "didn't wake up early"], ["didn't run", "was tired", "woke up early"], ["ran", "was not tired", "didn't wake up early"], ["ran", "was tired", "woke up early"]]

# We're trying to predict whether or not you were tired on this day
new_day = ["ran", "didn't wake up early"]

def calc_y_probability(y_label, days):
    return len([d for d in days if d[1] == y_label]) / len(days)

def calc_ran_probability_given_y(ran_label, y_label, days):
    return len([d for d in days if d[1] == y_label and d[0] == ran_label]) / len(days)

def calc_woke_early_probability_given_y(woke_label, y_label, days):
    return len([d for d in days if d[1] == y_label and d[2] == woke_label]) / len(days)

denominator = len([d for d in days if d[0] == new_day[0] and d[2] == new_day[1]]) / len(days)
# Plug all the values into our formula
# Multiply the class (y) probability, and the probability of the x-values occurring given that class
prob_tired = (calc_y_probability("was tired", days) * calc_ran_probability_given_y(new_day[0], "was tired", days) * calc_woke_early_probability_given_y(new_day[1], "was tired", days)) / denominator

prob_not_tired = (calc_y_probability("was not tired", days) * calc_ran_probability_given_y(new_day[0], "was not tired", days) * calc_woke_early_probability_given_y(new_day[1], "was not tired", days)) / denominator

# Make a classification decision based on the probabilities
classification = "was tired"
if prob_not_tired > prob_tired:
    classification = "was not tired"
print("Final classification for new day: {0}. Tired probability: {1}. Not tired probability: {2}.".format(classification, prob_tired, prob_not_tired))

## 3. Finding Word Counts ##

# A nice Python class that lets us count how many times items occur in a list
from collections import Counter
import csv
import re

# Read in the training data
with open("train.csv", 'r') as file:
    reviews = list(csv.reader(file))

def get_text(reviews, score):
    # Join together the text in the reviews for a particular tone
    # Lowercase the text so that the algorithm doesn't see "Not" and "not" as different words, for example
    return " ".join([r[0].lower() for r in reviews if r[1] == str(score)])

def count_text(text):
    # Split text into words based on whitespace -- simple but effective
    words = re.split("\s+", text)
    # Count up the occurrence of each word
    return Counter(words)

negative_text = get_text(reviews, -1)
positive_text = get_text(reviews, 1)
# Generate word counts for negative tone
negative_counts = count_text(negative_text)
# Generate word counts for positive tone
positive_counts = count_text(positive_text)

print("Negative text sample: {0}".format(negative_text[:100]))
print("Positive text sample: {0}".format(positive_text[:100]))

## 4. Making Predictions About Review Classifications ##

import re
from collections import Counter

def get_y_count(score):
    # Compute the count of each classification occurring in the data
    return len([r for r in reviews if r[1] == str(score)])

# We'll use these counts for smoothing when computing the prediction
positive_review_count = get_y_count(1)
negative_review_count = get_y_count(-1)

# These are the class probabilities (we saw them in the formula as P(y))
prob_positive = positive_review_count / len(reviews)
prob_negative = negative_review_count / len(reviews)

def make_class_prediction(text, counts, class_prob, class_count):
    prediction = 1
    text_counts = Counter(re.split("\s+", text))
    for word in text_counts:
        # For every word in the text, we get the number of times that word occurred in the reviews for a given class, add 1 to smooth the value, and divide by the total number of words in the class (plus the class_count, also to smooth the denominator)
        # Smoothing ensures that we don't multiply the prediction by 0 if the word didn't exist in the training data
        # We also smooth the denominator counts to keep things even
        prediction *=  text_counts.get(word) * ((counts.get(word, 0) + 1) / (sum(counts.values()) + class_count))
    # Now we multiply by the probability of the class existing in the documents
    return prediction * class_prob

# Now we can generate probabilities for the classes our reviews belong to
# The probabilities themselves aren't very useful -- we make our classification decision based on which value is greater
print("Review: {0}".format(reviews[0][0]))
print("Negative prediction: {0}".format(make_class_prediction(reviews[0][0], negative_counts, prob_negative, negative_review_count)))
print("Positive prediction: {0}".format(make_class_prediction(reviews[0][0], positive_counts, prob_positive, positive_review_count)))

## 5. Predicting the Test Set ##

import csv

def make_decision(text, make_class_prediction):
    # Compute the negative and positive probabilities
    negative_prediction = make_class_prediction(text, negative_counts, prob_negative, negative_review_count)
    positive_prediction = make_class_prediction(text, positive_counts, prob_positive, positive_review_count)

    # We assign a classification based on which probability is greater
    if negative_prediction > positive_prediction:
      return -1
    return 1

with open("test.csv", 'r') as file:
    test = list(csv.reader(file))

predictions = [make_decision(r[0], make_class_prediction) for r in test]

## 6. Computing Prediction Error ##

actual = [int(r[1]) for r in test]

from sklearn import metrics

# Generate the ROC curve using scikits-learn
fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)

# Measure the area under the curve
# The closer to 1 it is, the "better" the predictions
print("AUC of the predictions: {0}".format(metrics.auc(fpr, tpr)))

## 7. A Faster Way to Make Predictions ##

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics

# Generate counts from text using a vectorizer  
# We can choose from other available vectorizers, and set many different options
# This code performs our step of computing word counts
vectorizer = CountVectorizer(stop_words='english', max_df=.05)
train_features = vectorizer.fit_transform([r[0] for r in reviews])
test_features = vectorizer.transform([r[0] for r in test])

# Fit a Naive Bayes model to the training data
# This will train the model using the word counts we computed and the existing classifications in the training set
nb = MultinomialNB()
nb.fit(train_features, [int(r[1]) for r in reviews])

# Now we can use the model to predict classifications for our test features
predictions = nb.predict(test_features)

# Compute the error
# It's slightly different from our model because the internals of this process work differently from our implementation
fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
print("Multinomal naive bayes AUC: {0}".format(metrics.auc(fpr, tpr)))