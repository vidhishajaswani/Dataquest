## 1. Making a File ##


touch test.txt

## 2. Understanding Standard Streams ##


echo "All bears should juggle"

## 3. Redirecting Standard Streams ##


echo "All bears should juggle" > test.txt

## 4. Editing a File ##


#

## 5. Overview of File Permissions ##


ls -l

## 6. Octal Notation for File Permissions ##


stat test.txt

## 7. Modifying File Permissions ##


chmod 0760 test.txt

## 8. Moving Files ##


mkdir test
mv test.txt test

## 9. Copying Files ##


cp test/test.txt test/test2.txt

## 10. Overview of File Extensions ##


mv test/test.txt test/test_no_extension

## 11. Deleting a File ##


rm /home/dq/test/test2.txt

## 12. Bypassing Permissions as the Root User ##


sudo echo "Hello"