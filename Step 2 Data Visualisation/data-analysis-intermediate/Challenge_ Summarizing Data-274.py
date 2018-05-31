## 2. Introduction to the Data ##

import pandas as pd
all_ages=pd.read_csv("all-ages.csv")
recent_grads=pd.read_csv("recent-grads.csv")
print(all_ages[0:5])
print(recent_grads[0:5])



## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
#print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()

aa_unique=all_ages['Major_category'].unique()
rg_unique=recent_grads['Major_category'].unique()

for each in aa_unique:
    row=all_ages['Major_category']==each
    data=all_ages[row]
    aa_cat_counts[each]=data['Total'].sum()
    
for each in rg_unique:
    row=recent_grads['Major_category']==each
    data=recent_grads[row]
    rg_cat_counts[each]=data['Total'].sum()

## 4. Low-Wage Job Rates ##

low_wage_proportion=recent_grads["Low_wage_jobs"].sum()/recent_grads["Total"].sum()

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for each in majors:
    df_all_count=all_ages['Major']==each  
    df_all=all_ages[df_all_count]
    df_rg_count=recent_grads['Major']==each
    df_rg=recent_grads[df_rg_count]
    rg_rate=df_rg.iloc[0]['Unemployment_rate']
    all_rate=df_all.iloc[0]['Unemployment_rate']
    if rg_rate < all_rate :
        rg_lower_count+=1
        
print(rg_lower_count)