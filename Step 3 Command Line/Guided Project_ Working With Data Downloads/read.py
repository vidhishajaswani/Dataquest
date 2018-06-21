import pandas

if __name__ == "__main__":
    contents=pandas.read_csv('data/CRDC2013_14content.csv')
    print(contents.head())