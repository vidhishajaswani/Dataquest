## 1. Introduction to Version Control Systems ##


mkdir random_numbers
cd random_numbers
git init

## 2. The .git Folder ##


ls -al

## 3. Creating Files in the Repository ##


echo -e "Random number generator" > README.md
echo -e 'if __name__ == "__main__":\n    print("10")' > script.py

## 4. Checking File Status ##


git status
git add script.py
git add README.md

## 5. Configuring Identity in Git ##


git config --global user.email "user@dataquest.io"
git config --global user.name "Dataquest User"

## 6. Committing Changes ##


git commit -m "Initial commit.  Added script.py and README.md"

## 7. Viewing File Differences ##


echo -e 'import random\nif __name__ == "__main__":\n    print(random.randint(0,10))' > script.py
git status

## 8. Making a Second Commit ##


git add script.py
git commit -m "Made the numbers random"

## 9. Reviewing the Commit History ##


#

## 10. Viewing Commit Differences ##


#