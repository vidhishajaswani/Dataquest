## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')
wnba.head()
wnba.tail()
wnba.shape
parameter=max(wnba['Games Played'])
statistic=max(wnba['Games Played'].sample(n=30,random_state=1))
sampling_error=parameter-statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')
mean=wnba['PTS'].mean()
results=[]
for i in range(100):
    pts=wnba['PTS'].sample(n=10,random_state=i)
    results.append(pts.mean())
    
plt.scatter(x=range(1,101),y=results)
plt.axhline(mean)

## 7. Stratified Sampling ##

wnba['games_per_season']=wnba['PTS']/wnba['Games Played']
position=wnba['Pos'].unique()
position_most_points_dict={}
for each in position:
    pts=wnba[wnba['Pos']==each]['games_per_season'].sample(n=10,random_state=0)
    position_most_points_dict[each]=pts.mean()

position_most_points = max(position_most_points_dict, key = position_most_points_dict.get)

## 8. Proportional Stratified Sampling ##

first=wnba[wnba['Games Played']<=12]
second=wnba[(12<wnba['Games Played']) & (wnba['Games Played']<=22)]
third=wnba[wnba['Games Played']>22]
means=[]
for i in range(100):
    sample1=first.sample(1,random_state=i)
    sample2=second.sample(2,random_state=i)
    sample3=third.sample(7,random_state=i)
    
    all_samples=pd.concat([sample1,sample2,sample3])
    means.append(all_samples['PTS'].mean())
 
plt.scatter(range(1,101),means)
plt.axhline(wnba['PTS'].mean())


## 9. Choosing the Right Strata ##

wnba['MIN'].value_counts(bins = 3, normalize = True)

## 10. Cluster Sampling ##

teams=pd.Series(wnba['Team'].unique()).sample(4, random_state = 0)
df=pd.DataFrame()
for each in teams:
    df=df.append(wnba[wnba['Team']==each])
    
sampling_error_height=wnba['Height'].mean()-df['Height'].mean()
sampling_error_age=wnba['Age'].mean()-df['Age'].mean()
sampling_error_BMI=wnba['BMI'].mean()-df['BMI'].mean()
sampling_error_points=wnba['PTS'].mean()-df['PTS'].mean()