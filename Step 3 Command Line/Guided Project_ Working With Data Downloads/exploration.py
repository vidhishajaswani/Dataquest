import pandas as pd

if __name__ == "__main__":
    data=pd.read_csv('data/CRDC2013_14.csv',encoding="Latin-1")
    jj=pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")
    sch=pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum")
    print(jj)
    print(sch)
    
    
    
    