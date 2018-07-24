## 2. Calculating expected values ##

males_over50k=.669*.241 *32561
males_under50k=.669*.759*32561
females_over50k=.331*.241*32561
females_under50k=.331*.759*32561



## 3. Calculating chi-squared ##

observed = [6662, 1179, 15128, 9592]
expected = [5249.8, 2597.4, 16533.5, 8180.3]
values = []

for i, obs in enumerate(observed):
    exp = expected[i]
    value = (obs - exp) ** 2 / exp
    values.append(value)

chisq_gender_income = sum(values)

## 4. Finding statistical significance ##

from scipy.stats import chisquare
expected=[5249.8,2597.4,16533.5,8180.3]
observed=[6662,1179,15128,9592]
pvalue_gender_income=chisquare(observed,expected)

## 5. Cross tables ##

import pandas

table = pandas.crosstab(income["sex"], [income["race"]])
print(table)

## 6. Finding expected values ##

import pandas
from scipy.stats import chi2_contingency


table = pandas.crosstab(income["sex"], [income["race"]]) 
chisq_value, pvalue_gender_race, df,expected=chi2_contingency(table)
