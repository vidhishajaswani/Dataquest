## 2. Introduction To The Data ##

import pandas as pd
unrate=pd.read_csv("unrate.csv")
unrate["DATE"]=pd.to_datetime(unrate["DATE"])
print(unrate[0:12])

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt
plt.plot()
plt.show()

## 7. Adding Data ##

plt.plot(unrate[0:12]["DATE"], unrate[0:12]["VALUE"])
plt.show()

## 8. Fixing Axis Ticks ##

plt.plot(unrate[0:12]["DATE"], unrate[0:12]["VALUE"])
plt.xticks(rotation=90)

plt.show()


## 9. Adding Axis Labels And A Title ##

plt.plot(unrate[0:12]["DATE"], unrate[0:12]["VALUE"])
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()