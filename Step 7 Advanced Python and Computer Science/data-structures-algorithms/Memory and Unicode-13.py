## 2. The Basics of Binary ##

# Let's say b is a binary number.  In python, we have to store binary numbers as strings.
# If we try to enter it directly as b = 10, Python will assume it's a base 10 integer.
b = "10"

# Now, we can convert b from a string to a binary number with the int function. We'll need to set the optional second argument, base, to 2 (binary is base two).
print(int(b, 2))
base_10_100 = int("100", 2)

## 3. Binary Addition ##

# a is in base 10 -- because we have 10 possible digits, the highest value we can represent with one digit is 9.
a = 9

# When we want to represent a value one higher, we need to add another digit.
a += 1
# a now has two digits -- we incremented the invisible leading digit, which was 0 and is now 1, and set the last digit back to zero.
print(a)

# When we add 1 to 19, we increment the leading 1 by 1, and then set the last digit to 0, giving us 20.
a = 19
a += 1

# When we add 1 to 99, we increment the last digit by 1, and add 1 to the first digit, but the first digit is now greater than 9, so we have to increment the invisible leading digit.
a = 99
a += 1

# Binary addition works the exact same way, except the highest value any single digit can represent is 1.
b = "1"

# We'll add binary values using a binary_add function that was made just for this exercise.
# It's not extremely important to know how it works right this second.
def binary_add(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

c = binary_add(b, "1")

# We now see that c equals "10", which is exactly what happens in base 10 when we reach the highest possible digit.
print(c)

# c now equals "11"
c = binary_add(c, "1")
print(c)

# c now equals "100"
c = binary_add(c, "1")
print(c)

c = binary_add(c, "10")

## 4. Converting Binary Values to Other Bases ##

def binary_add(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

# Start both at 0
a = 0
b = "0"

# Loop 10 times
for i in range(0, 10):
    # Add 1 to each
    a += 1
    b = binary_add(b, "1")

    # Check if they are equal
    print(int(b, 2) == a)

# The cool thing here is that a and b are always equal if we add the same amount to both.
# This is because base 2 and base 10 are just ways to write numbers.
# Counting 100 apples in base 2 or base 10 will always give us an equivalent result - we just have to convert between them.
# We can represent any number in binary; we just need to use more digits than we would in base 10.
base_10_1001=int("1001",2)

## 5. Converting Characters to Binary ##

# We can use the ord() function to get the integer for an ASCII character.
ord('a')

# Then, we use the bin() function to convert to binary.
# The bin function adds "0b" to the beginning of a string to indicate that it contains binary values.
bin(ord('a'))

# ÿ is the "last" ASCII character; it has the highest integer value of any ASCII character.
# This is because 255 is the highest value we can represent with eight binary digits.
ord('ÿ')
# As you can see, we get eight 1's, which shows that this is the highest possible eight-digit value.
bin(ord('ÿ'))

# Why is this?  Because a single binary digit is called a bit, and computers store values in sequences of eight bits (i.e., a byte).
# You might be more familiar with kilobytes or megabytes. A kilobyte is 1000 bytes, and a megabyte is 1000 kilobytes.
# There are 256 different ASCII symbols, because the largest amount of storage any single ASCII character can take up is one byte.
binary_w=bin(ord('w'))
binary_bracket=bin(ord('}'))

## 6. Introduction to Unicode ##

# We can initialize Unicode code points (the value for this code point is \u27F6, but you see it as a character here because the Dataquest system is automatically converting it).
code_point = "⟶"

# This particular code point maps to a right arrow character.
print(code_point)

# We can get the base 10 integer value of the code point with the ord function.
print(ord(code_point))

# As you can see, this takes up a lot more than 1 byte.
print(bin(ord(code_point)))

binary_1019=bin(ord("\u1019"))

## 7. Strings with Unicode ##

s1 = "café"
# The \u prefix means "the next four digits are a Unicode code point"
# It doesn't change the value at all (the last character in the string below is \u00e9)
s2 = "café"

# These strings are the same, because code points are equal to their corresponding Unicode characters.
# \u00e9 and é are equivalent.
print(s1 == s2)
s3 = "hello မ"

## 8. The Bytes Data Type ##

# We can make a string with some Unicode values
superman = "Clark Kent␦"
print(superman)

# This tells Python to encode the string superman as Unicode using the UTF-8 encoding system
# We end up with a sequence of bytes instead of a string
superman_bytes = "Clark Kent␦".encode("utf-8")

batman = "Bruce Wayne␦"
batman_bytes=batman.encode("utf-8")

## 10. Hexadecimal Conversions ##

# F is the highest single digit in hexadecimal (base 16)
# Its value is 15 in base 10
print(int("F", 16))

# A in base 16 has the value 10 in base 10
print(int("A", 16))

# Just like the earlier binary_add function, this adds two hexadecimal numbers
def hexadecimal_add(a, b):
    return hex(int(a, 16) + int(b, 16))[2:]

# When we add 1 to 9 in hexadecimal, it becomes "a"
value = "9"
value = hexadecimal_add(value, "1")
print(value)

hex_ea=hexadecimal_add("ea","2")
hex_ef=hexadecimal_add("f","e")

## 11. Hex to Binary ##

# One byte (eight bits) in hexadecimal (the value of the byte below is \xe2)
hex_byte = "â"

# Print the base 10 integer value for the hexadecimal byte
print(ord(hex_byte))

# This gives the exact same value. Remember that \x is just a prefix, and doesn't affect the value.
print(int("e2", 16))

# Convert the base 10 integer to binary
print(bin(ord("â")))
binary_aa=bin(ord("\xaa"))
binary_ab=bin(ord("\xab"))

## 12. Bytes and Strings ##

hulk_bytes = "Bruce Banner␦".encode("utf-8")

# We can't mix strings and bytes
# For instance, if we try to replace the Unicode ␦ character as a string, it won't work, because that value has been encoded to bytes
try:
    hulk_bytes.replace("Banner", "")
except Exception:
    print("TypeError with replacement")

# We can create objects of the bytes data type by putting a b in front of the quotation marks in a string
hulk_bytes = b"Bruce Banner"
# Now, instead of mixing strings and bytes, we can use the replace method with bytes objects instead
hulk_bytes.replace(b"Banner", b"")

thor_bytes=b"Thor"

## 13. Decode Bytes to Strings ##

# Make a bytes object with aquaman's secret identity
aquaman_bytes = b"Who knows?"

# Now, we can use the decode method, along with the encoding system (UTF-8) to turn it into a string
aquaman = aquaman_bytes.decode("utf-8")

# We can print the value and type to verify that it's a string
print(aquaman)
print(type(aquaman))

morgan_freeman_bytes = b"Morgan Freeman"
morgan_freeman=morgan_freeman_bytes.decode("utf-8")

## 14. Read in File Data ##

# We can read our data in using csvreader
import csv
# When we open a file, we can specify the system used to encode it (in this case, UTF-8).
f = open("sentences_cia.csv", 'r', encoding="utf-8")
csvreader = csv.reader(f)
sentences_cia = list(csvreader)

# The data consists of two columns
# The first column contains the year, and the second contains a sentence from a CIA report written in that year
# Print the first column of the second row
print(sentences_cia[1][0])

# Print the second column of the second row
print(sentences_cia[1][1])

sentences_ten=sentences_cia[9][1]

## 15. Convert to a dataframe ##

import csv
# Let's read in the legislators data from a few missions ago
f = open("legislators.csv", 'r', encoding="utf-8")
csvreader = csv.reader(f)
legislators = list(csvreader)

# Now, we can import pandas and use the DataFrame class to convert the list of lists to a dataframe.
import pandas as pd

legislators_df = pd.DataFrame(legislators)

# As you can see, the first row contains the headers, which we don't want (because they're not actually data)
print(legislators_df.iloc[0,:])

# To remove the headers, we'll subset the df and pass them in separately
# This code removes the headers from legislators, and instead passes them into the columns argument
# The columns argument specifies column names
legislators_df = pd.DataFrame(legislators[1:], columns=legislators[0])
# We now have the right data in the first row, as well as the proper headers
print(legislators_df.iloc[0,:])

# The sentences_cia data from the last screen is available.
sentences_cia  = pd.DataFrame(sentences_cia[1:], columns=sentences_cia[0])


## 16. Clean up Sentences ##

# The integer codes for all the characters we want to keep
good_characters = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 32]

sentence_15 = sentences_cia["statement"][14]

# Iterate over the characters in the sentence, and only take those whose integer representations are in good_characters
# This will construct a list of single characters
cleaned_sentence_15_list = [s for s in sentence_15 if ord(s) in good_characters]

# Join the list together, separated by "" (no space), which creates a string again
cleaned_sentence_15 = "".join(cleaned_sentence_15_list)

def clean_statement(row):
    good_characters = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 32]
    s=row["statement"]
    clean=[st for st in s if ord(st) in good_characters]
    return "".join(clean)


sentences_cia["cleaned_statement"] = sentences_cia.apply(clean_statement, axis=1)
    

## 17. Tokenize Statements ##

# We can use the .join() method on strings to join lists together.
# The string we use the method on will become the separator -- the character(s) between each string when they are joined..
combined_statements = " ".join(sentences_cia["cleaned_statement"])

statement_tokens=combined_statements.split(" ")

## 18. Filter the Tokens ##

# statement_tokens has been loaded in.

filtered_tokens=[s for s in statement_tokens if len(s)>=5]

## 19. Count the Tokens ##

from collections import Counter
fruits = ["apple", "apple", "banana", "orange", "pear", "orange", "apple", "grape"]
fruit_count = Counter(fruits)

# Our code has counted each of the items in the list, and given them dictionary keys
print(fruit_count)

# filtered_tokens has been loaded in
filtered_token_counts=Counter(filtered_tokens)

## 20. Most Common Tokens ##

from collections import Counter
fruits = ["apple", "apple", "banana", "orange", "pear", "orange", "apple", "grape"]
fruit_count = Counter(fruits)

# We can use the most_common method of a Counter class to get the most common items
# We pass in a number, which is the number of items we want to get
print(fruit_count.most_common(2))
print(fruit_count.most_common(3))

# filtered_token_counts has been loaded in
common_tokens=filtered_token_counts.most_common(3)

## 21. Finding the Most Common Tokens by Year ##

# sentences_cia has been loaded in.
# It already has the cleaned_statement column.

from collections import Counter
def find_most_common_by_year(year, sentences_cia):
    data = sentences_cia[sentences_cia["year"] == year]
    combined_statement = " ".join(data["cleaned_statement"])
    statement_split = combined_statement.split(" ")
    counter = Counter([s for s in statement_split if len(s) > 4])
    return counter.most_common(2)

common_2000 = find_most_common_by_year("2000", sentences_cia)
common_2002 = find_most_common_by_year("2002", sentences_cia)
common_2013 = find_most_common_by_year("2013", sentences_cia)

