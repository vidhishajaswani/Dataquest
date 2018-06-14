## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()

true_avengers=avengers[avengers['Year']>=1960]

## 5. Consolidating Deaths ##

def clean_deaths(row):
    d=['Death1','Death2','Death3','Death4','Death5']
    NUM=0
    for each in d:
        death=row[each]
        if death == 'YES':
            NUM=NUM+1
        elif pd.isnull(death) or death == 'NO':
            continue
        
    return NUM
    
true_avengers['Deaths'] = true_avengers.apply(clean_deaths, axis=1)

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()
correct_joined_years = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]
joined_accuracy_count = len(correct_joined_years)