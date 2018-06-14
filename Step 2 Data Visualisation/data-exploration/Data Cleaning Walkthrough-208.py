## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
df=["ap_2010","class_size","demographics","graduation","hs_directory","sat_results"]
data = {}
for i in range(0,len(data_files)):
    data[df[i]]=pd.read_csv("schools/{0}".format(data_files[i]))
    

## 5. Exploring the SAT Data ##

data["sat_results"].head()

## 6. Exploring the Remaining Data ##

for each in data:
    print(data[each].head())

## 8. Reading in the Survey Data ##

all_survey=pandas.read_csv('schools/survey_all.txt',delimiter="\t",encoding="windows-1252")
d75_survey=pandas.read_csv('schools/survey_d75.txt',delimiter="\t",encoding="windows-1252")

survey=pandas.concat([all_survey,d75_survey],axis=0)
survey.head()

## 9. Cleaning Up the Surveys ##

survey["DBN"]=survey["dbn"]
data={}
cols=["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
survey=survey.loc[:,cols]
data["survey"]=survey

## 11. Inserting DBN Fields ##

data["hs_directory"]["DBN"]=data["hs_directory"]["dbn"]

def padded(col):
    str_col=str(col)
    for each in str_col:
        if len(str_col)>=2:
            return str_col
        elif len(str_col)==1:
            return str_col.zfill(2)
        
data["class_size"]["padded_csd"]=data["class_size"]["CSD"].apply(padded)
data["class_size"]["DBN"]=data["class_size"]["padded_csd"]+data["class_size"]["SCHOOL CODE"]
data["class_size"].head()

## 12. Combining the SAT Scores ##



data["sat_results"]["SAT Math Avg. Score"]=pd.to_numeric(data["sat_results"]["SAT Math Avg. Score"],errors="coerce")

data["sat_results"]["SAT Critical Reading Avg. Score"]=pd.to_numeric(data["sat_results"]["SAT Critical Reading Avg. Score"],errors="coerce")

data["sat_results"]["SAT Writing Avg. Score"]=pd.to_numeric(data["sat_results"]["SAT Writing Avg. Score"],errors="coerce")

data["sat_results"]["sat_score"]=data["sat_results"]["SAT Math Avg. Score"]+data["sat_results"]["SAT Critical Reading Avg. Score"]+data["sat_results"]["SAT Writing Avg. Score"]

data["sat_results"]["sat_score"].head()

## 13. Parsing Geographic Coordinates for Schools ##

import re

def myfunc(str):
    a=re.findall("\(.+\)",str)
    return a[0].split(',')[0].replace('(','')

data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(myfunc)
data["hs_directory"]["lat"].head()


## 14. Extracting the Longitude ##

import re

def myfunc2(str):
    a=re.findall("\(.+\)",str)
    return a[0].split(',')[1].replace(')','')

data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(myfunc2)
data["hs_directory"]["lon"]=pd.to_numeric(data["hs_directory"]["lon"],errors="coerce")
data["hs_directory"]["lat"]=pd.to_numeric(data["hs_directory"]["lat"],errors="coerce")