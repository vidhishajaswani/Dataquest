## 1. Booleans ##

cat=True
dog=False
print(type(cat))

## 2. Boolean Operators ##

print(cities)
first_alb= ("Albuquerque"==cities[0])
second_alb= ("Albuquerque"==cities[1])
first_last= (cities[len(cities)-1]==cities[0])


## 3. Booleans with "Greater Than" ##

print(crime_rates)
first_500=(crime_rates[0]>500)
first_749=(crime_rates[0]>=749)
first_last=(crime_rates[0]>=crime_rates[len(crime_rates)-1])

## 4. Booleans with "Less Than" ##

print(crime_rates)
second_500=(crime_rates[1]<500)
second_371=(crime_rates[1]<=371)
second_last=(crime_rates[1]<=crime_rates[len(crime_rates)-1])

## 5. If Statements ##

result = 0
if cities[2]=="Anchorage":
    result=1

## 6. Nesting If Statements ##

both_conditions = False
if crime_rates[0]>500:
    if crime_rates[1]>300:
        both_conditions=True
    

## 7. If Statements and For Loops ##

five_hundred_list=[]
for cr in crime_rates:
    if cr>500:
        five_hundred_list.append(cr)

## 8. Find the Highest Crime Rate ###

print(crime_rates)
highest=crime_rates[0]
for row in crime_rates:
    if row>highest:
        highest=row