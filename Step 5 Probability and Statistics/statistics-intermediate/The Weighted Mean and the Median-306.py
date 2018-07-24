## 1. Introduction ##

mean_new=houses_per_year['Mean Price'].mean()
mean_original = houses['SalePrice'].mean()
difference=mean_original - mean_new

## 2. Different Weights ##

houses_per_year['sum_per_year'] = houses_per_year['Mean Price'] * houses_per_year['Houses Sold']
all_sums_together = houses_per_year['sum_per_year'].sum()
total_n_houses = houses_per_year['Houses Sold'].sum()
weighted_mean = all_sums_together / total_n_houses

mean_original = houses['SalePrice'].mean()

difference = round(mean_original, 10) - round(weighted_mean, 10)

## 3. The Weighted Mean ##

def calc(means,weights):
    weighted_sum = []
    for mean, weight in zip(means, weights):
        weighted_sum.append(mean * weight)
    
    return sum(weighted_sum) / sum(weights)

weighted_mean_function = calc(houses_per_year['Mean Price'],houses_per_year['Houses Sold'])
from numpy import average
weighted_mean_numpy = average(houses_per_year['Mean Price'],
        weights = houses_per_year['Houses Sold'])

equal = round(weighted_mean_function, 10) == round(weighted_mean_numpy, 10)

## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']
median1=23
median2=55
median3=32

## 5. Distributions with Even Number of Values ##

ta=houses['TotRms AbvGrd'].copy()
ta=ta.replace({'10 or more':'10'})
ta=ta.astype(int)
ta=ta.sort_values()

middle_indices = [int((len(ta) / 2)),
                  int((len(ta) / 2 + 1))
                 ]
middle_values = ta.iloc[middle_indices] 
median = middle_values.mean()

## 6. The Median as a Resistant Statistic ##

houses['Lot Area'].plot.box()
houses['SalePrice'].plot.box()

lot_mean=houses['Lot Area'].mean()
sale_mean=houses['SalePrice'].mean()

lot_med=houses['Lot Area'].median()
sale_med=houses['SalePrice'].median()

lotarea_difference=lot_mean-lot_med
saleprice_difference=sale_mean-sale_med

## 7. The Median for Ordinal Scales ##

oc=houses['Overall Cond']
mean=oc.mean()
median=oc.median()

houses['Overall Cond'].plot.hist()
more_representative = 'mean' 


