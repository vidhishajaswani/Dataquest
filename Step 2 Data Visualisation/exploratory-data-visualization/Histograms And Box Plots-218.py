## 1. Introduction ##

import pandas as pd
import matplotlib.pyplot as plt
reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
norm_reviews = reviews[cols]
print(norm_reviews[:5])

## 2. Frequency Distribution ##

fandango_distribution=reviews['Fandango_Ratingvalue'].value_counts().sort_index()
imdb_distribution=reviews['IMDB_norm'].value_counts().sort_index()
print(fandango_distribution)
print(imdb_distribution)

## 4. Histogram In Matplotlib ##

fig,ax=plt.subplots()
ax.hist(norm_reviews['Fandango_Ratingvalue'], range=(0, 5))
plt.show()


## 5. Comparing histograms ##

fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.hist(norm_reviews['Fandango_Ratingvalue'],20,range=(0,5))
ax1.set_title('Distribution of Fandango Ratings')
ax1.set_ylim(0,50)


ax2.hist(norm_reviews['RT_user_norm'],20,range=(0,5))
ax2.set_title('Distribution of Rotten Tomatoes Ratings')
ax2.set_ylim(0,50)


ax3.hist(norm_reviews['Metacritic_user_nom'],20,range=(0,5))
ax3.set_title('Distribution of Metacritic Ratings')
ax3.set_ylim(0,50)


ax4.hist(norm_reviews['IMDB_norm'],20,range=(0,5))
ax4.set_title('Distribution of IMDB Ratings')
ax4.set_ylim(0,50)

plt.show()



## 7. Box Plot ##

fig,ax=plt.subplots()
ax.boxplot(norm_reviews['RT_user_norm'])
ax.set_ylim(0,5)
ax.set_xticklabels(['Rotten Tomatoes'])
plt.show()

## 8. Multiple Box Plots ##

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
fig,ax=plt.subplots()
ax.boxplot(norm_reviews[num_cols].values)
ax.set_ylim(0,5)
ax.set_xticklabels(num_cols,rotation=90)
plt.show()
