## 1. Introduction to Command Line Python ##


echo -e 'if __name__ == "__main__":\n    print("Welcome to a Python script")' > script.py
python script.py

## 2. Using Different Python Versions ##


python3 script.py

## 3. Installing Packages that Extend Python ##


pip install requests

## 4. Overview of Virtual Environments ##


virtualenv python2

## 5. Creating a Python 3 virtualenv ##


virtualenv -p /usr/bin/python3 python3

## 6. Activating a virtualenv ##


source python3/bin/activate

## 7. Verifying the Installed Packages ##


python -V

## 8. Importing Saved Functions into a File ##


echo -e 'def print_message():\n    print("Hello from another file!")' > utils.py
echo -e 'import utils\n\nif __name__ == "__main__":\n    utils.print_message()' > script.py
python script.py

## 9. Accessing Command Line Arguments ##


echo -e 'import sys\n\nif __name__ == "__main__":\n    print(sys.argv[1])' > script.py
python script.py "Hello from the command line"

## 10. Deactivating a virtualenv ##


deactivate