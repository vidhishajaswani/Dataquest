## 2. Bar Plots ##

exp=wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]]
exp.plot.bar()

## 3. Horizontal Bar Plots ##

exp=wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]]
exp.plot.barh(title='Number of players in WNBA by level of experience')

## 4. Pie Charts ##

exp=wnba['Exp_ordinal'].value_counts()
exp.plot.pie()

## 5. Customizing a Pie Chart ##

exp=wnba['Exp_ordinal'].value_counts()
exp.plot.pie(figsize = (6,6), autopct = '%.2f%%',title='Percentage of players in WNBA by level of experience')
plt.ylabel('')

## 6. Histograms ##

wnba['PTS'].plot.hist()

## 7. The Statistics Behind Histograms ##

wnba['Games Played'].describe()
wnba['Games Played'].plot.hist()

## 9. Binning for Histograms ##

wnba['Games Played'].plot.hist(range=(0,32),bins=8,title='The distribution of players by games played',xticks=range(0,33,4))
plt.xlabel('Games played')

## 10. Skewed Distributions ##

wnba['AST'].plot.hist()
wnba['FT%'].plot.hist()
assists_distro ='right skewed'
ft_percent_distro ='left skewed'

## 11. Symmetrical Distributions ##

wnba['MIN'].plot.hist()
normal_distribution ='Height'