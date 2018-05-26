## 3. Read the File Into a String ##

f=open('dq_unisex_names.csv','r')
names=f.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list=names.split("\n")
first_five=names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list=[]
for row in names_list:
    comma_list=row.split(',')
    nested_list.append(comma_list)
    
print(nested_list)

## 6. Convert Numerical Values ##

print(nested_list[0:5])
numerical_list=[]
for row in nested_list:
    temp=[]
    temp.append(row[0])
    temp.append(float(row[1]))
    numerical_list.append(temp)
print(numerical_list)

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater =[]
for row in numerical_list:
    if row[1]>=1000:
        thousand_or_greater.append(row[0])
print(thousand_or_greater[0:10])
    