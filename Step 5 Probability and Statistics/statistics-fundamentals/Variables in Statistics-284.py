## 2. Quantitative and Qualitative Variables ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')

variables = {'Name': 'qualitative', 'Team': 'qualitative', 'Pos': 'qualitative', 'Height': 'quantitative', 'BMI': 'quantitative',
             'Birth_Place': 'qualitative', 'Birthdate': 'quantitative', 'Age': 'quantitative', 'College': 'qualitative', 'Experience': 'quantitative',
             'Games Played': 'quantitative', 'MIN': 'quantitative', 'FGM': 'quantitative', 'FGA': 'quantitative',
             '3PA': 'quantitative', 'FTM': 'quantitative', 'FTA': 'quantitative', 'FT%': 'quantitative', 'OREB': 'quantitative', 'DREB': 'quantitative',
             'REB': 'quantitative', 'AST': 'quantitative', 'PTS': 'quantitative'}

## 4. The Nominal Scale ##

nominal_scale=sorted(['Name','Team','Birth_Place','Pos','College'])

## 5. The Ordinal Scale ##

question1=True
question2=False
question3=False
question4=True
question5=False
question6=False




## 7. The Difference Between Ratio and Interval Scales ##

interval=sorted(['Birthdate','Weight_deviation'])
ratio=sorted(['Height', 'Weight', 'BMI', 'Age', 'Experience', 'Games Played', 'MIN', 'FGM', 'FGA', 'FG%', '15:00', 
                '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TO',
                'PTS', 'DD2', 'TD3'])

## 9. Discrete and Continuous Variables ##

ratio_interval_only = {'Height': 'continuous', 'Weight': 'continuous', 'BMI': 'continuous', 'Age': 'continuous',
                       'Games Played': 'discrete', 'MIN': 'continuous', 'FGM': 'discrete',
                       'FGA': 'discrete', 'FG%': 'continuous', '3PA': 'discrete', '3P%': 'continuous',
                       'FTM': 'discrete', 'FTA': 'discrete', 'FT%': 'continuous', 'OREB': 'discrete',
                       'DREB': 'discrete', 'REB': 'discrete', 'AST': 'discrete', 'STL': 'discrete',
                       'BLK': 'discrete', 'TO': 'discrete', 'PTS': 'discrete', 'DD2': 'discrete', 
                       'TD3': 'discrete', 'Weight_deviation': 'continuous'}

## 10. Real Limits ##

bmi = {21.200991370000001: [21.2009913700000005, 21.2009913700000015],
 21.329437550000002: [21.3294375500000015, 21.3294375500000025],
 23.875432530000001: [23.8754325300000005, 23.8754325300000015],
 24.543462380000001: [24.5434623800000005, 24.5434623800000015],
 25.46938776: [25.469387755, 25.469387765]}