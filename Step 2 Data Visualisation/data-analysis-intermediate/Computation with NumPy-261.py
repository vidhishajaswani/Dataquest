## 2. Array Comparisons ##

countries_canada= world_alcohol[:,2]=='Canada'
years_1984=world_alcohol[:,0]=='1984'

## 3. Selecting Elements ##

country_is_algeria=world_alcohol[:,2]=='Algeria'
country_algeria=world_alcohol[country_is_algeria]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986=(world_alcohol [:,0]=='1986') & (world_alcohol [:,2]=='Algeria')
rows_with_algeria_and_1986=world_alcohol[is_algeria_and_1986]

## 5. Replacing Values ##

temp=world_alcohol[:,0]=='1986'
world_alcohol[:,0][temp]='2014'
temp2=world_alcohol[:,3]=='Wine'
world_alcohol[:,3][temp2]='Grog'

## 6. Replacing Empty Strings ##

is_value_empty=world_alcohol[:,4]==''
world_alcohol[is_value_empty,4]=0

## 7. Converting Data Types ##

alcohol_consumption=world_alcohol[:,4]
alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol=alcohol_consumption.sum()
average_alcohol=alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

is_canada_1986=(world_alcohol[:,0]=='1986') & (world_alcohol[:,2]=='Canada')
canada_1986 = world_alcohol[is_canada_1986,:]

canada_alcohol=canada_1986[:,4]
empty=canada_alcohol==''
canada_alcohol[empty]="0"
canada_alcohol=canada_alcohol.astype(float)
total_canadian_drinking=canada_alcohol.sum()


## 10. Calculating Consumption for Each Country ##

totals = {}
is_year=world_alcohol[:,0]=='1989'
year=world_alcohol[is_year,:]

for each in countries:
    temp=year[:,2]==each
    region=year[temp,:]
    consumption=region[:,4]
    a=consumption==''
    consumption[a]="0"
    consumption=consumption.astype(float)
    totals[each]=consumption.sum()
    
    
    

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
for each in totals:
    if totals[each]>highest_value:
        highest_key=each
        highest_value=totals[each]

