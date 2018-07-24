## 1. Individual Values ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')
houses['SalePrice'].plot.kde(xlim=(min(houses['SalePrice']),max(houses['SalePrice'])))
plt.axvline(houses['SalePrice'].mean(),color='Black',label='Mean')
plt.axvline(houses['SalePrice'].mean()+houses['SalePrice'].std(ddof=0),color='Red',label='Standard deviation')
plt.axvline(220000, color='Orange', label='220000')
plt.legend()
very_expensive=False

## 2. Number of Standard Deviations ##

mean=houses['SalePrice'].mean()
diff=220000-mean
st_devs_away=diff/houses['SalePrice'].std(ddof=0)

## 3. Z-scores ##

min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

def zscore(val,array,bessel=0):
    from numpy import std
    mean=sum(array)/len(array)
    sd=std(array,ddof=bessel)
    dist=val-mean
    return dist/sd

min_z=zscore(min_val,houses['SalePrice'])
mean_z=zscore(mean_val,houses['SalePrice'])
max_z=zscore(max_val,houses['SalePrice'])
    

## 4. Locating Values in Different Distributions ##

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z

NAmes=houses[houses['Neighborhood']=='NAmes']
CollgCr=houses[houses['Neighborhood']=='CollgCr']
OldTown=houses[houses['Neighborhood']=='OldTown']
Edwards=houses[houses['Neighborhood']=='Edwards']
Somerst=houses[houses['Neighborhood']=='Somerst']

print(z_score(200000,NAmes['SalePrice']))
print(z_score(200000,CollgCr['SalePrice']))
print(z_score(200000,OldTown['SalePrice']))
print(z_score(200000,Edwards['SalePrice']))
print(z_score(200000,Somerst['SalePrice']))

best_investment = 'College Creek'

## 5. Transforming Distributions ##

mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)
houses['z_prices'] = houses['SalePrice'].apply(
    lambda x: ((x - mean) / st_dev)
    )

z_mean_price=houses['z_prices'].mean()
z_stdev_price=houses['z_prices'].std(ddof=0)

mean_area = houses['Lot Area'].mean()
stdev_area = houses['Lot Area'].std(ddof = 0)
houses['z_area'] = houses['Lot Area'].apply(
    lambda x: ((x - mean_area) / stdev_area)
    )
z_mean_area=houses['z_area'].mean()
z_stdev_area=houses['z_area'].std(ddof=0)

## 6. The Standard Distribution ##

from numpy import std, mean
population = [0,8,0,8]
mean_p=mean(population)
std_p=std(population)
z=[]
for each in population:
    z.append((each-mean_p)/std_p)
    
mean_z=mean(z)
stdev_z=std(z)
    

## 7. Standardizing Samples ##

from numpy import std, mean
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 1)

standardized_sample = []
for value in sample:
    z = (value - x_bar) / s
    standardized_sample.append(z)
    
stdev_sample=std(standardized_sample,ddof=1)

## 8. Using Standardization for Comparisons ##

mean_index1 = houses['index_1'].mean()
stdev_index1 = houses['index_1'].std(ddof = 0)
houses['z_1'] = houses['index_1'].apply(
    lambda x: ((x - mean_index1) / stdev_index1)
    )

mean_index2 = houses['index_2'].mean()
stdev_index2 = houses['index_2'].std(ddof = 0)
houses['z_2'] = houses['index_2'].apply(
    lambda x: ((x - mean_index2) / stdev_index2)
    )

print(houses['z_1'].head())
print(houses['z_2'].head())
better = 'first'

## 9. Converting Back from Z-scores ##

m=50
sd=10
houses['x']=houses['z_merged'].apply(
                                lambda z: (z * sd + m)
                                )
mean_transformed=houses['x'].mean()
stdev_transformed=houses['x'].std(ddof=0)