## 1. Introduction ##


pwd
ls -l

## 2. Moving Problematic Files to a Separate Folder ##


mkdir /home/dq/problematic
mv /home/dq/crime_rates.json /home/dq/problematic/crime_rates.json
mv /home/dq/forest_fires.cssv /home/dq/problematic/forest_fires.cssv
mv /home/dq/legislators /home/dq/problematic/legislators

## 3. Fixing File Extensions ##


cd problematic/
mv crime_rates.json crime_rates.csv
mv forest_fires.cssv forest_fires.csv
mv legislators legislators.csv
ls -l

## 4. Consolidating Files ##


cd /home/dq/
mv nfl.csv problematic/nfl.csv
mv titanic_survival.csv problematic/titanic_survival.csv
mv problematic/ csv_datasets/

## 5. Restricting Permissions ##


cd /home/dq/csv_datasets
chmod 0740 nfl.csv
chmod 0740 titanic_survival.csv
chmod 0740 crime_rates.csv
chmod 0740 forest_fires.csv
chmod 0740 legislators.csv
ls -l