## 1. Comparing Frequency Distributions ##

# The WNBA dataset is already stored in the wnba variable
rookies = wnba[wnba['Exp_ordinal'] == 'Rookie']
little_xp = wnba[wnba['Exp_ordinal'] == 'Little experience']
experienced = wnba[wnba['Exp_ordinal'] == 'Experienced']
very_xp = wnba[wnba['Exp_ordinal'] == 'Very experienced']
veterans =  wnba[wnba['Exp_ordinal'] == 'Veteran']
rookie_distro = rookies['Pos'].value_counts()
little_xp_distro = little_xp['Pos'].value_counts()
experienced_distro = experienced['Pos'].value_counts()
very_xp_distro = very_xp['Pos'].value_counts()
veteran_distro = veterans['Pos'].value_counts()

print(rookie_distro, '\n\n', little_xp_distro, '\n\n', experienced_distro, '\n\n',
      very_xp_distro, '\n\n', veteran_distro)

## 2. Grouped Bar Plots ##

import seaborn as sns
sns.countplot(x = 'Exp_ordinal', hue = 'Pos', data = wnba,order = ['Rookie', 'Little experience', 'Experienced', 'Very experienced', 'Veteran'],
              hue_order = ['C', 'F', 'F/C', 'G', 'G/F'])

## 3. Challenge: Do Older Players Play Less? ##

import seaborn as sns
sns.countplot(x = 'age_mean_relative', hue = 'min_mean_relative',data=wnba)
result='rejection'

## 4. Comparing Histograms ##

import matplotlib.pyplot as plt
wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype = 'step', label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype = 'step', label = 'Young', legend = True)
plt.axvline(x=497,label='Average')
plt.legend()

## 5. Kernel Density Estimate Plots ##

wnba[wnba.Age >= 27]['MIN'].plot.kde(label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label = 'Young', legend = True)
plt.axvline(x=497,label='Average')
plt.legend()

## 7. Strip Plots ##

sns.stripplot(x = 'Pos', y = 'Weight', data = wnba, jitter = True)

## 8. Box plots ##

sns.boxplot(x = 'Pos', y = 'Weight', data = wnba)

## 9. Outliers ##

iqr=29-22
lower_bound=22-iqr*1.5
upper_bound=29+iqr*1.5
outliers_low = sum(wnba['Games Played'] < lower_bound)
outliers_high = sum(wnba['Games Played'] > upper_bound)
sns.boxplot(wnba['Games Played'])
