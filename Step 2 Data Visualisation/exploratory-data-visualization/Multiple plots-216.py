## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

plt.plot(unrate[0:12]["DATE"],unrate[0:12]["VALUE"])
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")

## 3. Matplotlib Classes ##

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

## 5. Adding Data ##

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)


ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax2 = fig.add_subplot(2,1,2)

ax2.plot(unrate[12:24]["DATE"],unrate[12:24]["VALUE"])
plt.show()

## 6. Formatting And Spacing ##

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
fig = plt.figure(figsize=(12, 5))
plt.show()

## 7. Comparing Across More Years ##

fig = plt.figure(figsize=(12, 12))

for i in range(5):
    ax1=fig.add_subplot(5,1,i+1)
    start=i*12
    end=(i+1)*12
    ax1.plot(unrate[start:end]['DATE'], unrate[start:end]['VALUE'])

plt.show()

## 8. Overlaying Line Charts ##

unrate['MONTH'] = unrate['DATE'].dt.month
fig = plt.figure(figsize=(6, 3))
#ax1=figure.add_plot(6,3,1)
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'],c="red")

#ax2=figure.add_plot(6,3,2)
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'],c="blue")

plt.show()



## 9. Adding More Lines ##

fig = plt.figure(figsize=(10, 6))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'],c="red")
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'],c="blue")
plt.plot(unrate[24:36]['MONTH'], unrate[24:36]['VALUE'],c="green")
plt.plot(unrate[36:48]['MONTH'], unrate[36:48]['VALUE'],c="orange")
plt.plot(unrate[48:60]['MONTH'], unrate[48:60]['VALUE'],c="black")




## 10. Adding A Legend ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    label=1948+i
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i],label=label)
    
plt.legend(loc='upper left')
plt.show()

## 11. Final Tweaks ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.show()