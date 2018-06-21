
import pandas as pd

if __name__ == "__main__":
    data=pd.read_csv('data/CRDC2013_14.csv',encoding="Latin-1")
    race=['HI','AM','AS','HP','BL','WH','TR']
    gender=['F','M']
    data['total_enrollment']=data['TOT_ENR_M']+data['TOT_ENR_F']
    all_enrollment=sum(data['total_enrollment'])
    totals={}
    for each in race:
        sum_f="SCH_ENR_"+each+"_"+gender[0]
        sum_m="SCH_ENR_"+each+"_"+gender[1]
        total="total_"+each
        totals[total]=100*(data[sum_m].sum() + data[sum_f].sum()) / all_enrollment
        
    for k,v in totals.items():
        print(k,v)
        
    
    