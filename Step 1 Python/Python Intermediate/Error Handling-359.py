## 2. Sets ##

gender=[]
for each in legislators:
    gender.append(each[3])
    
    
gender=set(gender)
print(gender)

## 3. Exploring the Dataset ##

party=[]
for each in legislators:
    party.append(each[6])
    
party=set(party)
print(party)
print(legislators)
    
    

## 4. Missing Values ##

for each in legislators:
    if each[3]=='':
        each[3]='M'
 
gender=[]
for each in legislators:
    gender.append(each[3])
    
print(set(gender))
    

## 5. Parsing Birth Years ##

birth_years=[]

for each in legislators:
    parts=each[2].split('-')
    birth_years.append(parts[0])
    

## 6. Try/except Blocks ##

try:
    float('hello')
except Exception:
    
    print('Error converting to float.')

## 7. Exception Instances ##

try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))

    

## 8. The Pass Keyword ##

converted_years = []

for year in birth_years:
    try:
        int_year=int(year)
        converted_years.append(int_year)
    except Exception:
        pass

## 9. Convert Birth Years to Integers ##

for each in legislators:
    birthday=each[2].split('-')
    try:
        birth_year=int(birthday[0])
    except Exception:
        birth_year=0
    each.append(birth_year)
        
       
    

## 10. Fill in Years Without a Value ##

last_value=1
for each in legislators:
    if each[7]==0:
        each[7]=last_value
    last_value=each[7]