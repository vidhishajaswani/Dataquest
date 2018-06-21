## 1. Introduction ##


cd ..
cd ~
pwd

## 2. Create a Script ##


echo -e 'import sys\n\nif __name__ == "__main__":\n    print(sys.argv[1])' > script.py

## 3. Change File Permissions ##


chmod 0700 script.py

## 4. Create a Virtual Environment ##


virtualenv -p /usr/bin/python3 script
source script/bin/activate

## 5. Move the Script ##


mkdir printer
mv script.py printer

## 6. Execute the Script ##


cd printer
python script.py "I'm so good at challenges!"